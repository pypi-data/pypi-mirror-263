import multiprocessing
import os
import time

import threading

from queue import Queue as tQueue
from multiprocessing import Process, Event
from multiprocessing import Queue as mQueue

from config_rt import ConfigRT

from DataSource.datasource_factory import create_data_source
from Processors.processor_factory import create_data_processor
from Consumers.consumer_factory import create_data_consumer

from DataFaceApp import run_frontend

from Frontend.frontend_factory import create_frontend

import signal


def sigint(SignalNumber, Frame):
    print("CNTRL+C Pressed!")
    DataFaceController.global_stop_event.set()


signal.signal(signal.SIGINT, sigint)


class DataFaceController:
    """
    Controller class.
    Handles creation and running of all processes/threads.
    Sets interprocess communication queues
    """

    global_stop_event = threading.Event()

    def __init__(self):
        """
        DataFaceController  Constructor
        :param mode: "add" or Any "add" enables adding a new person's face data in db
        """
        # Application services
        self.data_source = None
        self.frontends = []
        self.services = {}

    def run(self) -> None:
        """ Starts all services and keeps running """

        # Start frontends
        for f in self.frontends:
            f.start()
            f.wait2run()

        # Start all services, excluding frontends and datasource
        for p_list in self.services.values():
            for p in p_list:
                if p != self.data_source and p not in self.frontends:
                    p.start()
                    p.wait2run()

        # All services started, now start datasource
        if self.data_source is not None:
            self.data_source.start()

        while not DataFaceController.global_stop_event.is_set():
            if not self.is_running():
                break
            time.sleep(1)

        self.stop()

    def stop(self) -> None:
        """ Stops all services """
        print("       xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        print("       xxxxxxxx Stopping all services xxxxxxxx")
        print("       xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx")
        for p_list in self.services.values():
            for p in p_list:
                if p is not None and p.is_alive():
                    p.stop()
                    p.join()

    def is_running(self) -> bool:
        """ Checks if we need to continue to run all services """
        for p_list in self.services.values():
            for p in p_list:
                if p is not None and p.is_alive():
                    return True
        print("Not running!")
        return False

    def config(self, config_name) -> bool:
        """ Init all services according to config """
        try:
            cfg = ConfigRT(config_name, autostart=False)
        except Exception as e:
            print("DataFaceController: config: " + str(e))
            return False

        if cfg.get('multiprocessing', False):
            Queue = mQueue  # use multiprocessing q
        else:
            Queue = tQueue  # use standard thread-safe q

        try:
            data_source = cfg.get('data_source', {'id': None, 'config': None})
            source_id, source_cfg = (data_source['id'], data_source['config'])
        except Exception as e:
            print("controller: No data source set in config " + config_name)
            return False

        processors = cfg.get('processors', [])
        consumers  = cfg.get('consumers', [])
        frontends  = cfg.get('frontends', [])

        connections = cfg.get('data_connections', [])

        # Init a datasource
        try:
            if source_id is not None:
                self.data_source = create_data_source(source_id, Queue(), source_cfg)
                self.services[source_id] = [self.data_source]
        except Exception as e:
            print(f"Controller: config: Failed to init datasource: " + str(e))
            return False

        # Init processors
        for proc in processors:
            proc_id, proc_cfg = (proc['id'], proc['config'])
            n_proc = proc.setdefault('n_proc', 0)
            try:
                self.services[proc_id] = create_data_processor(proc_id, proc_cfg, Queue(), n_proc)
            except Exception as e:
                print(f"Controller: config: Failed to init processor {proc_id}: " + str(e))
                return False

        # Init consumers
        for cons in consumers:
            cons_id, cons_cfg = (cons['id'], cons['config'])
            try:
                self.services[cons_id] = create_data_consumer(cons_id, Queue(), cons_cfg)
            except Exception as e:
                print(f"Controller: config: Failed to init consumer {cons_id}: " + str(e))
                return False

        for front in frontends:
            front_id, front_cfg = front['id'], front['config']
            try:
                f = create_frontend(front_id, front_cfg)
                self.services[front_id] = f
                self.frontends.extend(f)
            except Exception as e:
                print(f"Controller: config: Failed to init frontend {front_id}: " + str(e))
                return False

        # Establish data connections
        for c in connections:
            try:
                src_list = self.services[c[0]['id']]
                dst = self.services[c[1]['id']][0]
                for src in src_list:
                    try:
                        src.add_q_out(dst.proc_id, dst.q_in)
                    except TypeError:
                        src.add_q_out(dst.q_in)

            except Exception as e:
                print(f"Controller: config: Failed to establish pipeline {c[0]}, {c[1]}: " + str(e))

        # Clear console before proceeding
        time.sleep(1)
        os.system("cls")

        return True


from copy import deepcopy

class Task(object):
    def __init__(self, id  , successors, speed_on_core , predecessors=None):
        """ parameters:
            id, predecessors, successors,
            speeds on core and speeds on cloud,
            finish times, ready times, etc
            """
        self.id = id
        self.predecessors = predecessors
        self.successors = successors
        """ initialize finish time"""
        self.finish_time_init()
        """ init ready time """
        self.ready_time_init()
        """ init speeds """
        self.speeds_init(speed_on_core)
        """ other params"""
        self.on_device = True

        """ use pr_val for determine priority"""
        self.pr_val = None
        """ use assignment for determine which local or cloud, value ->[0,3] """
        self.assignment = -1
        """ use start time for determine start time on locals or cloud, core1, core2, core3, cloud"""
        self.start_time = [-1, -1, -1, -1]
        """ temp value for check kernel algorithm """
        self.check_kernel = None
        """ temp value for priority score"""
        self.w_i = 0

    def finish_time_init(self):
        self.ft_l = 0


    def ready_time_init(self):
        """ local ready time and ..."""
        self.ready_time = -1


    def speeds_init(self, speed_on_core ):
        """ speeds on cores """
        self.speed_on_core = speed_on_core


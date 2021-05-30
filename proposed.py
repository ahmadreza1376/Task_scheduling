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
        self.speeds_init(speed_on_core, [3, 1, 1])
        """ other params"""
        self.on_device = None
        """ determine local or cloud """
        self.on_local_or_cloud()
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
        self.ft_ws = 0
        self.ft_c = 0
        self.ft_wr = 0

    def ready_time_init(self):
        """ local ready time and ..."""
        self.ready_time = -1
        self.rt_ws = -1
        self.rt_c = -1
        self.rt_wr = -1

    def speeds_init(self, speed_on_core , speed_on_cloud):
        """ speeds on cores """
        self.speed_on_core = speed_on_core
        self.speed_on_cloud = speed_on_cloud  # list [3, 1, 1] cloud speed

    def on_local_or_cloud(self):
        """local or cloud, core3 is fastest and cloud is always 5"""
        t_l_min = self.speed_on_core[2]
        t_c_min = 5
        if t_l_min <= t_c_min:
            self.on_device = True
            self.ft_ws = 0
            self.ft_c = 0
            self.ft_wr = 0
        else:
            self.on_device = False
            self.ft_l = 0
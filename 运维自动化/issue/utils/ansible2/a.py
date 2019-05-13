#!/usr/bin/env python

import json
from collections import namedtuple
from ansible.parsing.dataloader import DataLoader
from ansible.vars.manager import VariableManager
from ansible.inventory.manager import InventoryManager
from ansible.executor.playbook_executor import PlaybookExecutor
from ansible.plugins.callback import CallbackBase
from ansible.playbook.play import Play
from ansible.executor.task_queue_manager import TaskQueueManager


class PlaybookResultsCallback(CallbackBase):
    def __init__(self, *args, **kwargs):
        super(PlaybookResultsCallback, self).__init__(*args, **kwargs)
        self.task_ok = {}
        self.task_unreachable = {}
        self.task_failed = {}
        self.task_skipped = {}
        self.task_stats = {}

    def v2_runner_on_unreachable(self, result):
        self.task_unreachable[result._host.get_name()] = result

    def v2_runner_on_ok(self, result, *args, **kwargs):
        self.task_ok[result._host.get_name()] = result

    def v2_runner_on_failed(self, result, *args, **kwargs):
        self.task_failed[result._host.get_name()] = result

    def v2_runner_on_skipped(self, result, *args, **kwargs):
        self.task_skipped[result._host.get_name()] = result

    def v2_runner_on_stats(self, result, *args, **kwargs):
        self.task_stats[result._host.get_name()] = result


class ResultsCallback(CallbackBase):
    def __init__(self, *args, **kwargs):
        super(ResultsCallback, self).__init__(*args, **kwargs)
        self.host_ok = {}
        self.host_unreachable = {}
        self.host_failed = {}

    def v2_runner_on_unreachable(self, result):
        self.host_unreachable[result._host.get_name()] = result

    def v2_runner_on_ok(self, result, *args, **kwargs):
        self.host_ok[result._host.get_name()] = result

    def v2_runner_on_failed(self, result, *args, **kwargs):
        self.host_failed[result._host.get_name()] = result


# chushihua
class Runner(object):
    def __init__(self, *args, **kwargs):
        self.loader = DataLoader()
        self.results_callback = ResultsCallback()
        self.Playbook_results_callback = PlaybookResultsCallback()
        self.inventory = InventoryManager(loader=self.loader, sources=['/etc/ansible/hosts'])
        self.variable_manager = VariableManager(loader=self.loader, inventory=self.inventory)
        self.passwords = None
        self.results_raw = {}

        Options = namedtuple('Options',
                             ['connection',
                              'remote_user',
                              'ask_sudo_pass',
                              'verbosity',
                              'ack_pass',
                              'module_path',
                              'forks',
                              'become',
                              'become_method',
                              'become_user',
                              'check',
                              'listhosts',
                              'listtasks',
                              'listtags',
                              'syntax',
                              'sudo_user',
                              'sudo',
                              'diff'])
        # 初始化需要的对象
        self.options = Options(connection='smart',
                               remote_user=None,
                               ack_pass=None,
                               sudo_user=None,
                               forks=5,
                               sudo=None,
                               ask_sudo_pass=False,
                               verbosity=5,
                               module_path=None,
                               become=None,
                               become_method=None,
                               become_user=None,
                               check=False,
                               diff=False,
                               listhosts=None,
                               listtasks=None,
                               listtags=None,
                               syntax=None)

    def run_ad_hoc(self):
        play_source = dict(
            name="Ansible Play ad-hoc",
            hosts='test',
            gather_facts='no',
            tasks=[
                dict(action=dict(module='shell', args='ls /home'), register='shell_out'),
                # dict(action=dict(module='debug', args=dict(msg='{{shell_out.stdout}}')))
            ]
        )
        play = Play().load(play_source, variable_manager=self.variable_manager, loader=self.loader)

        tqm = None
        try:
            tqm = TaskQueueManager(
                inventory=self.inventory,
                variable_manager=self.variable_manager,
                loader=self.loader,
                options=self.options,
                passwords=self.passwords,
                stdout_callback=self.results_callback,
            )
            result = tqm.run(play)
        finally:
            if tqm is not None:
                tqm.cleanup()

        ##定义字典用于接收或者处理结果

    def get_adhoc_result(self):
        self.results_raw = {'success': {}, 'failed': {}, 'unreachable': {}}
        for host, result in self.results_callback.host_ok.items():
            hostvisiable = host.replace('.', '_')
            self.results_raw['success'][hostvisiable] = result._result

        for host, result in self.results_callback.host_failed.items():
            hostvisiable = host.replace('.', '_')
            self.results_raw['failed'][hostvisiable] = result._result

        for host, result in self.results_callback.host_unreachable.items():
            hostvisiable = host.replace('.', '_')
            self.results_raw['unreachable'][hostvisiable] = result._result
        return self.results_raw

    def run_playbook(self, extra_vars=None):
        if extra_vars: self.variable_manager.extra_vars = extra_vars
        playbook = PlaybookExecutor(playbooks=['/Users/derekwang/test/a.yml'], inventory=self.inventory,
                                    variable_manager=self.variable_manager,
                                    loader=self.loader, options=self.options, passwords=self.passwords)

        playbook._tqm._stdout_callback = self.Playbook_results_callback
        results = playbook.run()

    def get_playbook_result(self):
        ##定义字典用于接收或者处理结果
        self.result_raw = {'success': {}, 'failed': {}, 'unreachable': {}, 'skipped': {}, 'status': {}}

        # 循环打印这个结果，success，failed，unreachable需要每个都定义一个
        for host, result in self.Playbook_results_callback.task_ok.items():
            self.result_raw['success'][host] = result._result

        for host, result in self.Playbook_results_callback.task_failed.items():
            self.result_raw['failed'][host] = result._result

        for host, result in self.Playbook_results_callback.task_unreachable.items():
            self.result_raw['unreachable'][host] = result._result

        for host, result in self.Playbook_results_callback.task_skipped.items():
            self.result_raw['skipped'][host] = result._result

        for host, result in self.Playbook_results_callback.task_stats.items():
            self.result_raw['status'][host] = result._result

        return self.result_raw


c = Runner()

c.run_ad_hoc()
c.run_playbook()
print(c.get_adhoc_result(), c.get_playbook_result())

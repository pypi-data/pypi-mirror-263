#
# Pavlin Georgiev, Softel Labs
#
# This is a proprietary file and may not be copied,
# distributed, or modified without express permission
# from the owner. For licensing inquiries, please
# contact pavlin@softel.bg.
#
# 2023
#

import os

from sciveo.common.tools.logger import *
from sciveo.common.sampling import RandomSampler, GridSampler, AutoSampler
from sciveo.content.project import RemoteProject, LocalProject


class ProjectRunner:
  current = None

  def __init__(self, project, function, configuration={}, **kwargs):
    self.project_name = project
    self.function = function
    self.kwargs = kwargs

    self.arguments = {
      'count': None,
      'remote': True,
      'sampler': "random",
      'num_random_samples': 10,
      'next_sample_ratio': 0.97,
      'min_delta_score': 1e-5,
      'optimizer': "base",
      'learning_rate': 0.1,
      'learning_rate_decay': 0.01
    }

    self.count = self.get('count')
    remote = self.get('remote')
    sampler = self.get('sampler')

    if remote:
      self.project = RemoteProject(self.project_name)
    else:
      self.project = LocalProject(self.project_name)

    if sampler == "random":
      self.configuration_sampler = RandomSampler(configuration)
    elif sampler == "grid":
      self.configuration_sampler = GridSampler(configuration)
    elif sampler == "auto":
      self.configuration_sampler = AutoSampler(
        configuration, self.project,
        num_random_samples=self.get('num_random_samples'),
        next_sample_ratio=self.get('next_sample_ratio'),
        min_delta_score=self.get('min_delta_score'),
        optimizer=self.get('optimizer'),
        learning_rate=self.get('learning_rate'),
        learning_rate_decay=self.get('learning_rate_decay')
      )
    else:
      self.configuration_sampler = RandomSampler(configuration)

    debug(type(self).__name__, f"start remote[{remote}] count[{self.count}] sampler[{sampler}]", configuration)

  def get(self, a):
    return self.kwargs.get(a, self.arguments[a])

  def describe(self):
    return {
      "arguments": self.arguments,
      "sampler": self.configuration_sampler.describe()
    }

  def run(self):
    for i, configuration_sample in enumerate(self.configuration_sampler):
      if self.count is not None and i >= self.count:
        break

      self.project.config = configuration_sample
      self.project.config.set_name(f"[{self.project.list_content_size + i + 1}]")
      debug(type(self).__name__, "run", i, self.project.config)
      self.function()

# coding=utf-8

from django_cron import CronJobBase, Schedule

from .crawler import run


class CrawlTwitterCronJob(CronJobBase):
    # every hours
    RUN_EVERY_MINS = 30
    # retry
    RETRY_AFTER_FAILURE_MINS = 5
    schedule = Schedule(run_every_mins=RUN_EVERY_MINS, retry_after_failure_mins=RETRY_AFTER_FAILURE_MINS)
    code = 'api.cronjob'

    def do(self):
        run()

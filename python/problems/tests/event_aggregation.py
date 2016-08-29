import random
import unittest2

from problems.event_aggregation import CountService
from problems.event_aggregation import DAYS
from problems.event_aggregation import HOURS
from problems.event_aggregation import MINUTES
from problems.event_aggregation import SECONDS


class EventTimeSeriesTestCase(unittest2.TestCase):
    def setUp(self):
        self.service = CountService()
        self.event_names = [
            'tweet',
            'retweet',
            'follow',
        ]
        print "Register random events every seconds for 2 days"
        for i in range(0, 2 * DAYS, SECONDS):
            event_name = random.choice(self.event_names)
            self.service.register_event(event_name, i)

    def _humanize(self, granularity):
        if granularity == SECONDS:
            return "second"
        if granularity == MINUTES:
            return "minute"
        if granularity == HOURS:
            return "hour"
        if granularity == DAYS:
            return "day"

        return granularity

    def _pluralize(self, word):
        return "%ss" % word

    def _test_granularity(self, granularity, event_name, start, end):
        delta = int((end - start) / granularity)
        humanized_granularity = self._humanize(granularity)
        print "Get %s count for %s %s by %s" % (
            event_name,
            delta,
            self._pluralize(humanized_granularity),
            humanized_granularity
        )
        ret = self.service.get_count_for_time_range(granularity, event_name, start, end)
        self.assertEqual(delta, len(ret))
        print ret

    def test_minute_granularity(self):
        start = 0 * DAYS + 0 * HOURS + 30 * MINUTES
        end = start + 10 * MINUTES
        self._test_granularity(MINUTES, 'tweet', start, end)

    def test_hour_granularity(self):
        start = 0 * DAYS + 1 * HOURS
        end = start + 2 * HOURS
        self._test_granularity(HOURS, 'retweet', start, end)

    def test_day_granularity(self):
        start = 0 * DAYS
        end = start + 2 * DAYS
        self._test_granularity(DAYS, 'follow', start, end)


if __name__ == '__main__':
    unittest2.main()

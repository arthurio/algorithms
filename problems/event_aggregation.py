from collections import defaultdict


# Variable to translate from milliseconds
SECONDS = 1000
MINUTES = 60 * SECONDS
HOURS = 60 * MINUTES
DAYS = 24 * HOURS


class HashableGranularity:
    """ This class is used to hash a time from a range to the starting time of that range based on the granularity.
        For example, for a given time_in_millis 1000 and 1500 if the MODULO is 1000 (1s), they would produce the same
        hash.
    """
    def __init__(self, time_in_millis, modulo):
        """ Parameters
            time_in_millis: Integer
        """
        self.modulo = modulo
        self.time_in_millis = time_in_millis

    def __hash__(self):
        return self.time_in_millis - (self.time_in_millis % self.modulo)

    def __eq__(self, other):
        return self.__hash__() == other.__hash__()

    def __str__(self):
        return str(self.time_in_millis)


class CountService:
    """ This class is used to register events and aggregate them by granularities.
    """

    GRANULARITIES = (
        MINUTES,
        HOURS,
        DAYS,
    )

    def __init__(self):
        """ Initialize the data structure to store our aggregated counts by event.
            if we register 2 events with time_in_millis == 1000
            e.g.
            {
                HOURS: {
                    0: {
                        'tweet': 2,
                        'follow': 3,
                    }
                    ...
                },
                MINUTES: {
                    0: {
                        'tweet': 2,
                        'follow': 3,
                    }
                    ...
                }
                ...
            }
        """
        self.aggregations = {
            granularity: defaultdict(lambda: defaultdict(int))
            for granularity in CountService.GRANULARITIES
        }

    def register_event(self, event_name, time_in_millis):
        for granularity, aggregation in self.aggregations.items():
            key_object = HashableGranularity(time_in_millis, granularity)
            aggregation[key_object][event_name] += 1

    def get_count_for_time(self, granularity, event_name, time_in_millis):
        assert(granularity in self.GRANULARITIES)
        key_object = HashableGranularity(time_in_millis, granularity)
        aggregation = self.aggregations[granularity]
        if key_object not in aggregation:
            return 0
        return self.aggregations[granularity][key_object].get(event_name, 0)

    def get_count_for_time_range(self, granularity, event_name, start_time_in_millis, end_time_in_millis):
        assert(granularity in self.GRANULARITIES)
        return[
            self.get_count_for_time(granularity, event_name, time_in_millis)
            for time_in_millis in range(start_time_in_millis, end_time_in_millis, granularity)
        ]

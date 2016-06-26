from Queue import Queue
from threading import Thread


class AsyncExternalDataLoader:
    """
    Allows performing multiple actions in an async way, ideal to do multiple external api calls in parallel.
    Create a thread per action allowing all of them to run at the same time.

    If self._num_fetch_threads = 1 all the actions will be excecuted one at a time simulating a regular sequential
    execution:

        --- 0.000169038772583 seconds --- init photos download
        --- 0.90238904953 seconds --- end photos download
        --- 0.902453184128 seconds --- init posts download
        --- 1.60568118095 seconds --- end posts download
        --- 1.60580420494 seconds --- init users download
        --- 2.11058807373 seconds --- end users download

    If self._num_fetch_threads = 3, 3 threads will be enabled to process elements in parallel so all the actions
    will start practically at the same time:

        --- 0.000602960586548 seconds --- init photos download
        --- 0.000463962554932 seconds --- init posts download
        --- 0.000311136245728 seconds --- init users download
        --- 0.50043296814 seconds --- end users download
        --- 0.700552940369 seconds --- end posts download
        --- 0.900881052017 seconds --- end photos download
        ---------------------------------------------------------------------

    """

    def __init__(self, data_dict):
        """
        :param data_dict: Dict, contains the actions to be executed in an async way. ATTENTION: All the actions have to
        be lambda calls Ie.
            {
                "users": lambda: api_one_instance.get_users(),
                "posts": lambda: api_one_instance.get_posts(),
                "photos": lambda: api_one_instance.get_photos()
            }
        """
        self._data_dict = data_dict
        self._retrieved_data_dict = {}
        self._num_fetch_threads = len(data_dict)
        self._queue = Queue()

    @staticmethod
    def __perform_load(queue_obj, retrieved_data_dict):
        """
        Execute the action and notify the queue that the action is completed. Once the execution is done, the result
        is saved in retrieved_data_dict
        :param retrieved_data_dict: Dict, object where is stored the result of every excecuted action.. Ie
            {
                "users": [...],
                "posts": [...],
                "photos": [...]
            }
        """

        while True:
            queued_action = queue_obj.get()
            queued_action_key = queued_action[0]
            queued_action_lambda = queued_action[1]
            retrieved_data_dict[queued_action_key] = queued_action_lambda()
            queue_obj.task_done()

    def __setup_threads(self):
        """
        Create threads based on the number of the keys of the data_dict. Each thread act as a worker that is
        constantly looking if there are elements in the query to be processed
        """
        for i in range(self._num_fetch_threads):
            worker = Thread(target=self.__perform_load, args=(self._queue, self._retrieved_data_dict))
            worker.setDaemon(True)
            worker.start()

    def __feed_queue(self):
        """
        Add the actions to the queue
        """
        for key, value in self._data_dict.iteritems():
            self._queue.put((key, value))

    def async_load_data(self):
        """
        Setup threads, queue and execute the parallel call of the actions
        :return: Dict, result of the calls that were excecuted in an async way. Ie
            {
                "users": [...],
                "posts": [...],
                "photos": [...]
            }
        """

        # create threads to be used for async processing
        self.__setup_threads()

        # add actions to the queue
        self.__feed_queue()

        # Now wait for the queue to be empty, indicating that all the actions where performed
        self._queue.join()

        return self._retrieved_data_dict

import time


class ApiOne(object):

    @staticmethod
    def get_users():
        """
        Simulate the call to an api to the "/users" endpoint, it supposedly takes 0.5 seconds
        :return: List with the retrieved users. Ie
            [
                {'name': 'Peter', 'last_name': 'Greenberg'},
                {'name': 'John', 'last_name': 'Smith'}
            ]
        """
        # instead of really connecting to an api and downloading users we just pretend and sleep
        time.sleep(0.5)
        return [
            {'name': 'Peter', 'last_name': 'Greenberg'},
            {'name': 'John', 'last_name': 'Smith'}
        ]

    @staticmethod
    def get_photos():
        """
        Simulate the call to an api to the "/photos" endpoint, it supposedly takes 0.9 seconds
        :return: List with the retrieved photos. Ie
            [
                {
                    'name': 'Cute bull terrier puppy 1',
                    'url': 'http://thehappypuppysite.com/wp-content/uploads/2015/08/white-Bull-Terrier-pup.jpg'
                }, {
                    'name': 'Cute bull terrier puppy 2',
                    'url': 'http://3.bp.blogspot.com/-2fAHTmTM5dM/VP5fQlQ_7fI/AAAAAAAABss/ohcBkUqhTpw/s1600/bullmalo.jpg'
                }
            ]
        """
        # instead of really connecting to an api and downloading photos we just pretend and sleep
        time.sleep(0.9)
        return [
            {
                'name': 'Cute bull terrier puppy 1',
                'url': 'http://thehappypuppysite.com/wp-content/uploads/2015/08/white-Bull-Terrier-pup.jpg'
            }, {
                'name': 'Cute bull terrier puppy 2',
                'url': 'http://3.bp.blogspot.com/-2fAHTmTM5dM/VP5fQlQ_7fI/AAAAAAAABss/ohcBkUqhTpw/s1600/bullmalo.jpg'
            }
        ]

    @staticmethod
    def get_posts():
        """
        Simulate the call to an api to the "/posts" endpoint, it supposedly takes 0.7 seconds
        :return: List with the retrieved photos. Ie
            [
                {'title': 'My first post', 'content': 'I love my dog'},
                {'title': 'Damn', 'content': 'The dog is chewing my shoe :/'}
            ]
        """
        # instead of really connecting to an api and downloading posts we just pretend and sleep
        time.sleep(0.7)
        return [
            {'title': 'My first post', 'content': 'I love my dog'},
            {'title': 'Damn', 'content': 'The dog is chewing my shoe :/'}
        ]

"""
    Sample Controller File

    A Controller should be in charge of responding to a request.
    Load models to interact with the database and load views to render them to the client.

    Create a controller using this template
"""
from system.core.controller import *
import random
class Ninja(Controller):
    def __init__(self, action):
        super(Ninja, self).__init__(action)
        """
            This is an example of loading a model.
            Every controller has access to the load_model method.

            self.load_model('WelcomeModel')
        """

    """ This is an example of a controller method that will load a view for the client """
    def index(self):
        try:
            session['gold']
            session['history']
        except:
            session['gold'] = 0
            session['history'] = []
        """ 
        A loaded model is accessible through the models attribute 
        self.models['WelcomeModel'].get_all_users()
        """
        return self.load_view('index.html')

    def makegold(self):
        location_list ={'farm':(10, 20), 'cave':(5, 10), 'house':(2, 5), 'casino':(-50, 50)}
        profit = random.randint(*location_list[request.form['location']])
        session['gold'] += profit
        if profit < 0:
            cssclass = 'lost'
        else:
            cssclass = 'won'

        session['history'].append({'location':request.form['location'], 'profit': profit, 'cssclass':cssclass})
        return redirect('/')

    def reset(self):
        session['gold'] = 0
        session['history'] = []
        return redirect('/')
import numpy as np

class Agent:

    def __init__(self, image0, image1, imageG):
        self.im_0 = image0
        self.im_1 = image1
        self.im_G = imageG

        self.state = 0          #0=0-image, 1=1-image, 2=gaussian image
        self.last_im = []       #last image which was sampled (according to current state)
        self.a = 0              #transition probability after taking action a
        self.b = 0.5            #transition probability after taking action b
        self.action_prob = 0.4  #probability of choosing action a
        

    def do_step(self):
        action = self.get_action()
        s1 = self.state
        im1 = self.last_im
        s2 = s1
        if(action == 'b'):      #only when action b is chosen we probably switch state
            ran_num = np.random.uniform(low=0.0, high=1.0)
            if(ran_num <= self.b):
                s2 = self.switch_state()
        self.state = s2

        index = 0
        im2 = []
        if(s2 == 0):
            index = np.random.randint(low=0, high=len(self.im_0))
            im2 = self.im_0[index]
        else:
            index = np.random.randint(low=0, high=len(self.im_G))
            im2 = self.im_G[index]
        self.last_im = im2    
        
        return (im1, action, im2)

    def get_action(self):
        action = 'a'
        if(np.random.uniform(low=0.0, high=1.0) > self.action_prob):
            action = 'b'
        return action

    def switch_state(self):
        state = 0
        if(self.state == 0):
            state = 2
        return state

a = Agent([[1,2]],[[3,4]],[[5,6]])
for i in range(10):
    x = a.do_step()
    print(x,'\n')


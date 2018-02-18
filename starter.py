import cgp_core
import cgp_zmq
import json
import time
from newplot import *
import matplotlib.pyplot as plt
import matplotlib.animation as animation
from matplotlib import style


fig1 = plt.figure(1)
ax1 = fig1.add_subplot(1, 1, 1)
fig2 = plt.figure(2)
ax2 = fig2.add_subplot(1, 1, 1)
fig3 = plt.figure(3)
ax3 = fig3.add_subplot(1, 1, 1)
data = {}

def animate(i):
    plt.figure(1)
    global data
    global locations
    ax1.clear()
    plt.title(data['name'])
    plt.ylabel('Count')
    plt.xlabel('City')
    yticks = []
    yvalues = []
    for k, v in locations.items():
        if (v > 0):
            yvalues.append(v)
            vals = k.split(',')
            if (len(vals) == 1):
                yticks.append(vals[0])
            elif (len(vals) >= 2):
                yticks.append(vals[1])
                # yticks.append(k)
    xvalues = range(len(yvalues))

    plt.bar(xvalues, yvalues, width=0.5)
    plt.xticks(range(len(yticks)), yticks)


def animate2(i):
    plt.figure(2)
    technologies,name=find_count_by_technology(data)
    ax1.clear()
    plt.title(name)
    plt.ylabel('Count')
    plt.xlabel('Technology')
    yticks=technologies.keys()
    yvalues=technologies.values()
    xvalues=range(len(yvalues))

    plt.bar(xvalues,yvalues,width=0.5)
    #plt.xticks(range(len(yticks)),yticks)

def animate3(i):
    plt.figure(3)
    wins,name=find_count_by_winners(data)
    ax1.clear()
    plt.title(name)
    plt.ylabel('Count')
    plt.xlabel('location')
    yticks=wins.keys()
    for i in range(len(yticks)):
        if yticks[i].strip(' ') in us_state_abbrev.keys():
            yticks[i]=us_state_abbrev[yticks[i].strip(' ')]
    vals=wins.values()
    participants=[]
    winners=[]
    for i in vals:
        participants.append(i[0])
        winners.append(i[1])
    xvalues=range(len(vals))

    plt.bar(xvalues,participants,color='r',width=0.5)
    plt.bar(xvalues,winners,bottom=participants,color='g',width=0.5)
    plt.xticks(range(len(yticks)),yticks)




count = 2
# Application class deriveed from cgp_core.Application
class Application(cgp_core.Application):
    # on_consume method to expect the Reaction data from Adapter
    def on_consume(self, responses):
        global count,list_popular_x,list_popular_y

        popularity (responses[-1]['vqts'][0])
        #print locations

        get_x_axis_popular()
        get_x_axis_popular()


        global data

        data = responses[-1]['vqts'][0]

        #print responses[-1]['vqts']['name']

        a.add('Tag00', 0, 'cgp://adp1', 'a', count, 5000, 0, None, None, None, None)
        count = count + 1

        self.send_request(a)

if __name__ == "__main__":
    # build request
    a = cgp_core.ActionData('')
    a.add('Tag00', 0, 'cgp://adp1', 'a', 1, 5000, 0, None, None, None, None)
    # send request
    app = Application()
    appComm = cgp_zmq.ApplicationComm('app3', 'tcp://127.0.0.1:3000')
    app.instrument = appComm
    time.sleep(5)
    print 'sending'
    app.send_request(a)
    ani = animation.FuncAnimation(plt.figure(1), animate, interval=4000)
    ani2 = animation.FuncAnimation(plt.figure(2), animate2, interval=4000)
    ani3 = animation.FuncAnimation(plt.figure(3), animate3, interval=4000)
    style.use('fivethirtyeight')
    colours = 'bgrbgrbgrb'
    plt.figure(1)
    plt.show()
    plt.figure(2)
    plt.show()
    plt.figure(3)
    plt.show()

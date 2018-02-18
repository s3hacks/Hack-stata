def animate(i):
    global x
    a = get_json_line(x)
    popularity(a)
    get_x_axis_popular()
    ax1.clear()
    plt.title(a['name'])
    plt.ylabel('Count')
    plt.xlabel('City')
    yticks=[]
    yvalues=[]
    for k,v in locations.items():
        if(v>0):
            yvalues.append(v)
            vals=k.split(',')
            if(len(vals)==1):
                yticks.append(vals[0])
            elif(len(vals)>=2):
                yticks.append(vals[1])
            #yticks.append(k)
    xvalues=range(len(yvalues))
    if(len(yticks)==0):
        x=x+1
        a = get_json_line(x)
        popularity(a)
        get_x_axis_popular()
        yticks=[]
        yvalues=[]
        for k,v in locations.items():
            if(v>0):
                yvalues.append(v)
                vals=k.split(',')
                if(len(vals)==1):
                    yticks.append(vals[0])
                elif(len(vals)>=2):
                    yticks.append(vals[1])
                #yticks.append(k)
        xvalues=range(len(yvalues))
        print yticks
        print yvalues
        print xvalues
        plt.bar(xvalues,yvalues,width=0.5)
        plt.xticks(range(len(yticks)),yticks)
        x+=1
    else:
        print yticks
        print yvalues
        print xvalues
        plt.bar(xvalues,yvalues,width=0.5)
        plt.xticks(range(len(yticks)),yticks)
        x+=1
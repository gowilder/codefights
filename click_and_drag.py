import math
def multiSelection(dimensions, tasks, mouseCoordinates):
    total_tasks = len(tasks)
    print 'total tasks: ' + str(total_tasks)
    click_xmax = max(mouseCoordinates[0][0],mouseCoordinates[1][0])
    click_xmin = min(mouseCoordinates[0][0],mouseCoordinates[1][0])
    click_ymax = max(mouseCoordinates[0][1],mouseCoordinates[1][1])
    click_ymin = min(mouseCoordinates[0][1],mouseCoordinates[1][1])
    print 'click_ymax: '  + str(click_ymax)
    height_selection = click_ymax - click_ymin
    print 'height_selection: ' + str(height_selection)

    if height_selection >= dimensions[2]:
        print 'There are tasks inside'
        if click_ymin <= dimensions[1]:
            first_task = 0
        else:
            first_task = (click_ymin - (dimensions[1]+dimensions[2]))/float(dimensions[1]+dimensions[2])
            print first_task
            first_task = math.ceil(first_task)
            print int(first_task)
        last_task = (click_ymax - (dimensions[1]+dimensions[2]))/float(dimensions[1]+dimensions[2])
        last_task = math.trunc(last_task) + 1
        print int(last_task)
        print click_ymin, click_ymax
        return tasks[int(first_task):int(last_task)+1]

    else:
        if 
        return []

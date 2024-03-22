event_queue = []
listeners_mapping = dict()


def register_listeners(listeners):
    global listeners_mapping
    listeners_mapping = listeners


def fire_event(evt):
    global listeners_mapping
    global event_queue

    from .listener import Listener
    for k, v in listeners_mapping.items():
        if k == type(evt):
            if type(v) is list:
                for lst in v:
                    lst().handle(evt)
            elif issubclass(v, Listener):
                v().handle(evt)


def fire_all_postponed():
    global listeners_mapping
    global event_queue

    for evt in event_queue:
        fire_event(evt)

    event_queue.clear()

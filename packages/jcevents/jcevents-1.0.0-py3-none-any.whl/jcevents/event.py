class Event(object):
    def __init__(self, **kwargs):
        for k, v in kwargs.items():
            setattr(self, k, v)

    def fire(self):
        from .queue import fire_event
        fire_event(self)

    def postpone(self):
        from .queue import event_queue
        if self not in event_queue:
            event_queue.append(self)

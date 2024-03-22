jcevents Library Documentation
=============================

Introduction
------------
The ``jcevents`` library is a lightweight event-driven framework for Python that allows you to implement event handling and listeners in your applications. This documentation provides a guide on how to use the library effectively.

Installation
------------
You can install the ``jcevents`` library using pip:

.. code-block:: bash

    pip install jcevents

Getting Started
---------------
To begin using the ``jcevents`` library, follow these steps:

1. Import the necessary modules:

.. code-block:: python

    import jcevents
    from jcevents import Event, Listener, register_listeners, fire_all_postponed

2. Define your custom events by inheriting from the ``Event`` class and implementing the required logic:

.. code-block:: python

    class MyEvent(Event):
        def __init__(self, success: bool):
            super(MyEvent, self).__init__()
            self.success = success

3. Implement event listeners by inheriting from the ``Listener`` class and overriding the ``handle`` method:

.. code-block:: python

    class MyListener(Listener):
        def handle(self, event: MyEvent):
            if event.success:
                print("> Event success !!!")
            else:
                print("> Event not success")

4. Register your event listeners with their corresponding events using the ``register_listeners`` function:

.. code-block:: python

    register_listeners({
        MyEvent: MyListener
    })

5. Create instances of your events, postpone them if needed, and then fire all postponed events using ``fire_all_postponed``:

.. code-block:: python

    my_event = MyEvent(success=True)
    my_event.postpone()
    fire_all_postponed()

Example Usage
-------------
Here's an example demonstrating how to use the ``jcevents`` library in a Python script:

.. code-block:: python

    import jcevents
    from jcevents import Event, Listener, register_listeners, fire_all_postponed

    class MyEvent(Event):
        def __init__(self, success: bool):
            super(MyEvent, self).__init__()
            self.success = success

    class MyListener(Listener):
        def handle(self, event: MyEvent):
            if event.success:
                print("> Event success !!!")
            else:
                print("> Event not success")

    def main():
        register_listeners({
            MyEvent: MyListener
        })
        my_event = MyEvent(success=True)
        my_event.postpone()
        fire_all_postponed()

    if __name__ == "__main__":
        main()

Conclusion
-----------
The ``jcevents`` library provides a simple yet powerful way to implement event-driven architecture in your Python applications. By defining custom events, implementing event listeners, and using the provided functions, you can easily manage and handle events in your projects.

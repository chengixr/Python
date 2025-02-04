import stomp
import pygame

conn = stomp.Connection([('124.220.233.252', 61613)])
conn.connect('admin', 'admin', wait=True)
message = 'Hello, world!'
conn.send(destination='/queue/test1', body=message)
conn.disconnect()
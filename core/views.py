from django.shortcuts import render, HttpResponse

def hello(request):
  return HttpResponse('Hello World')

def add(request, number1, number2):
  return HttpResponse('The sum of {} + {} is {}'.format(number1, number2, (number1+number2)))

def subtract(request, number1, number2):
  return HttpResponse('The subtraction of {} - {} is {}'.format(number1, number2, (number1-number2)))

def multiply(request, number1, number2):
  return HttpResponse('The multiplication of {} * {} is {}'.format(number1, number2, (number1*number2)))

def divide(request, number1, number2):
  return HttpResponse('The division of {} / {} is {}'.format(number1, number2, (number1/number2)))
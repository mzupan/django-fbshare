# Django-FBShare

## Overview

This is a simple module I did to teach learn template tags in Django. I know its very simple to
just place the markup and javascript in the template but I like simple and this is simple and
easy to change. 

## Installation

To install simply clone the project and the easy thing to do is place the project in your Django
project directory

Then in settings.py add the following to your INSTALLED_APPS

projectname.django-sharefb

## Usage

Always load the script in your template

{% load fbshare %}

### Link

{% fbshare link %}

### Button with no counter

{% fbshare button %}

### Button with inline counter

{% fbshare button counter %}

### Button with counter above it

{% fbshare button counter above %}

## Known Issues

If your page has no links sometimes the counter just doesn't show up. Right now I'm not doing much 
error checking
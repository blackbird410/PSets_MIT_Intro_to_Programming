# 6.0001/6.00 Problem Set 5 - RSS Feed Filter
# Name: Neil Taison RIGAUD
# Collaborators: None
# Time: 10:05 AM ~ ...

import feedparser
import string
import time
import threading
from project_util import translate_html
from mtTkinter import *
from datetime import datetime
from copy import copy
import pytz
import collections
collections.Callable = collections.abc.Callable

#-----------------------------------------------------------------------

#======================
# Code for retrieving and parsing
# Google and Yahoo News feeds
# Do not change this code
#======================

def process(url):
    """
    Fetches news items from the rss url and parses them.
    Returns a list of NewsStory-s.
    """
    feed = feedparser.parse(url)
    entries = feed.entries
    ret = []
    for entry in entries:
        guid = entry.guid
        title = translate_html(entry.title)
        link = entry.link
        description = translate_html(entry.description)
        pubdate = translate_html(entry.published)

        try:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %Z")
            pubdate.replace(tzinfo=pytz.timezone("GMT"))
          #  pubdate = pubdate.astimezone(pytz.timezone('EST'))
          #  pubdate.replace(tzinfo=None)
        except ValueError:
            pubdate = datetime.strptime(pubdate, "%a, %d %b %Y %H:%M:%S %z")

        newsStory = NewsStory(guid, title, description, link, pubdate)
        ret.append(newsStory)
    return ret

#======================
# Data structure design
#======================

# Problem 1

# TODO: NewsStory
class NewsStory:

    def __init__(self, guid, title, description, link, pubdate):
        """Initialize a NewsStory instance.

        guid: A string for the global unique identifier of the news.
        title: A string for the title of the news story.
        description: A string describing the story.
        link: A link to the full content of the news story.
        pubdate: A datetime value for the date of publication of the news story.

        """

        self.guid = guid
        self.title = title
        self.description = description
        self.link = link
        self.pubdate = pubdate
        self.pubdate = self.pubdate.replace(tzinfo=pytz.timezone("EST"))

    # Defining the getters
    def get_guid(self):
        return self.guid

    def get_title(self):
        return self.title

    def get_description(self):
        return self.description

    def get_link(self):
        return self.link

    def get_pubdate(self):
        return self.pubdate


#======================
# Triggers
#======================

class Trigger(object):
    def evaluate(self, story):
        """
        Returns True if an alert should be generated
        for the given news item, or False otherwise.
        """
        # DO NOT CHANGE THIS!
        raise NotImplementedError

# PHRASE TRIGGERS

# Problem 2
class PhraseTrigger(Trigger):
    def __init__(self, phrase):
        self.phrase = phrase

    def is_phrase_in(self, story):
        # Make a copy of the story
        copy_story = copy(story)
        phrase = self.phrase.lower()

        # Formatting the text
        for x in string.punctuation:
            copy_story = copy_story.replace(x, " ")
        copy_story = " ".join(copy_story.split()).lower()

        # Find the string in the text
        index = copy_story.find(phrase)
        story_length = len(copy_story)

        if index >= 0:
            end_index = index + len(phrase)
            if end_index < story_length:
                return True if copy_story[end_index] == " " else False
            else:
                return True

        return False

    def evaluate(self, story):
        return self.is_phrase_in(story)


# Problem 3
class TitleTrigger(PhraseTrigger):
    def __init__(self, title):
        self.phrase = title

    def evaluate(self, news_story):
        return self.is_phrase_in(news_story.get_title())


# Problem 4
class DescriptionTrigger(PhraseTrigger):
    def __init__(self, description):
        self.phrase = description

    def evaluate(self, news_story):
        return self.is_phrase_in(news_story.get_description())

# TIME TRIGGERS

# Problem 5
class TimeTrigger(Trigger):
    def __init__(self, time):
        if time[1] == " ":
            time = "0" + time

        self.time = datetime.strptime(time, "%d %b %Y %H:%M:%S")
        self.time = self.time.replace(tzinfo=pytz.timezone("EST"))
        


# Problem 6
class BeforeTrigger(TimeTrigger):
    def evaluate(self, news_story):
        return self.time > news_story.get_pubdate()

class AfterTrigger(TimeTrigger):
    def evaluate(self, news_story):
        return self.time < news_story.get_pubdate()


# COMPOSITE TRIGGERS

# Problem 7
class NotTrigger(Trigger):
    def __init__(self, other_trigger):
        self.other_trigger = other_trigger

    def evaluate(self, story):
        return not self.other_trigger.evaluate(story)

# Problem 8
class AndTrigger(Trigger):
    def __init__(self, first_trigger, second_trigger):
        self.first_trigger = first_trigger
        self.second_trigger = second_trigger

    def evaluate(self, story):
        return self.first_trigger.evaluate(story) and self.second_trigger.evaluate(story)

# Problem 9
class OrTrigger(Trigger):
    def __init__(self, first_trigger, second_trigger):
        self.first_trigger = first_trigger
        self.second_trigger = second_trigger

    def evaluate(self, story):
        return self.first_trigger.evaluate(story) or self.second_trigger.evaluate(story)


#======================
# Filtering
#======================

# Problem 10
def filter_stories(stories, triggerlist):
    """
    Takes in a list of NewsStory instances.

    Returns: a list of only the stories for which a trigger in triggerlist fires.
    """
    filtered_stories = []
    for story in stories:
        for trigger in triggerlist:
            if trigger.evaluate(story):
                filtered_stories.append(story)
                break

    return filtered_stories



#======================
# User-Specified Triggers
#======================
# Problem 11
def read_trigger_config(filename):
    """
    filename: the name of a trigger configuration file

    Returns: a list of trigger objects specified by the trigger configuration
        file.
    """
    # We give you the code to read in the file and eliminate blank lines and
    # comments. You don't need to know how it works for now!
    trigger_file = open(filename, 'r')
    lines = []
    for line in trigger_file:
        line = line.rstrip()
        if not (len(line) == 0 or line.startswith('//')):
            lines.append(line)

    triggers_list = []
    triggers_dict = {}
    for line in lines:
        current_line = line.split(",")
        # If it is a trigger
        if current_line[0] != "ADD":
            # If it is a PhraseTrigger
            if current_line[1] in ["TITLE", "DESCRIPTION"]:
                triggers_dict[current_line[0]] = {"trigger_type": current_line[1], "phrase": current_line[2]}
            elif current_line[1] in ["AFTER", "BEFORE"]:
                triggers_dict[current_line[0]] = {"trigger_type": current_line[1], "time": current_line[2]}
            elif current_line[1] in ["AND", "OR"]:
                triggers_dict[current_line[0]] = {"trigger_type": current_line[1], "first_trigger": current_line[2], "second_trigger": current_line[3]}
            elif current_line[1] == "NOT":
                triggers_dict[current_line[0]] = {"trigger_type": current_line[1], "trigger_param": current_line[2]}
        else:
            # Add the triggers to the list
            triggers = current_line[1:]
            for t in triggers:
                triggers_list.append(get_trigger(triggers_dict, t))

    return triggers_list

def get_trigger(triggers_dict, t):
    trigger = triggers_dict[t]
    if trigger["trigger_type"] == "TITLE":
        return TitleTrigger(trigger["phrase"])
    elif trigger["trigger_type"] == "DESCRIPTION":
        return DescriptionTrigger(trigger["phrase"])
    elif trigger["trigger_type"] == "BEFORE":
        return BeforeTrigger(trigger["time"])
    elif trigger["trigger_type"] == "AFTER":
        return AfterTrigger(trigger["time"])
    elif trigger["trigger_type"] == "NOT":
        param_t = triggers_dict[trigger["trigger_param"]]
        return NotTrigger(get_trigger(triggers_dict, param_t))
    elif trigger["trigger_type"] == "OR":
        t1 = triggers_dict[trigger["first_trigger"]]
        t2 = triggers_dict[trigger["second_trigger"]]
        return OrTrigger(get_trigger(triggers_dict, t1), get_trigger(triggers_dict, t2))
    else:
        t1 = trigger["first_trigger"]
        t2 = trigger["second_trigger"]
        return AndTrigger(get_trigger(triggers_dict, t1), get_trigger(triggers_dict, t2))
    

SLEEPTIME = 120 #seconds -- how often we poll

def main_thread(master):
    # A sample trigger list - you might need to change the phrases to correspond
    # to what is currently in the news
    try:
        t1 = TitleTrigger("election")
        t2 = DescriptionTrigger("Trump")
        t3 = DescriptionTrigger("Clinton")
        t4 = AndTrigger(t2, t3)
        triggerlist = [t1, t4]

        # Problem 11
        # TODO: After implementing read_trigger_config, uncomment this line 
        triggerlist = read_trigger_config('triggers.txt')
        
        # HELPER CODE - you don't need to understand this!
        # Draws the popup window that displays the filtered stories
        # Retrieves and filters the stories from the RSS feeds
        frame = Frame(master)
        frame.pack(side=BOTTOM)
        scrollbar = Scrollbar(master)
        scrollbar.pack(side=RIGHT,fill=Y)

        t = "Google & Yahoo Top News"
        title = StringVar()
        title.set(t)
        ttl = Label(master, textvariable=title, font=("Helvetica", 18))
        ttl.pack(side=TOP)
        cont = Text(master, font=("Helvetica",14), yscrollcommand=scrollbar.set)
        cont.pack(side=BOTTOM)
        cont.tag_config("title", justify='center')
        button = Button(frame, text="Exit", command=root.destroy)
        button.pack(side=BOTTOM)
        guidShown = []
        def get_cont(newstory):
            if newstory.get_guid() not in guidShown:
                cont.insert(END, newstory.get_title()+"\n", "title")
                cont.insert(END, "\n---------------------------------------------------------------\n", "title")
                cont.insert(END, newstory.get_description())
                cont.insert(END, "\n*********************************************************************\n", "title")
                guidShown.append(newstory.get_guid())

        while True:

            print("Polling . . .", end=' ')
            # Get stories from Google's Top Stories RSS news feed
            stories = process("http://news.google.com/news?output=rss")

            # Get stories from Yahoo's Top Stories RSS news feed
            # stories.extend(process("http://news.yahoo.com/rss/topstories"))

            stories = filter_stories(stories, triggerlist)

            list(map(get_cont, stories))
            scrollbar.config(command=cont.yview)


            print("Sleeping...")
            time.sleep(SLEEPTIME)

    except Exception as e:
        print(e)


if __name__ == '__main__':
    root = Tk()
    root.title("Some RSS parser")
    t = threading.Thread(target=main_thread, args=(root,))
    t.start()
    root.mainloop()


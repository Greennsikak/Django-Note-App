from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Topic, Entry
from .forms import TopicForm, EntryForm

# Create your views here.

@login_required
def topic(request):
    topics = Topic.objects.filter(owner=request.user).order_by('date_added')
    context = {'topics': topics}
    return render(request, "Note/topic.html", context)

@login_required
def topics(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    entries = topic.entry.all()
    context = {'topic': topic, 'entries': entries}
    return render(request, "Note/topics.html", context)

@login_required
def new_topic(request):
    if request.method == "POST":
        form = TopicForm(data=request.POST)
        if form.is_valid():
            new_topic = form.save(commit=False)
            new_topic.owner = request.user
            new_topic.save()
            return redirect('Note:topic')
    else:
        form = TopicForm()
    return render(request, "Note/new.html", {'form': form})

@login_required
def del_topic(request, topic_id):
    del_topic = Topic.objects.get(id=topic_id)
    del_topic.delete()
    return redirect("Note:topic")

@login_required
def new_entry(request, topic_id):
    topic = Topic.objects.get(id=topic_id)
    if request.method != "POST":
        form = EntryForm()

    else:
        form = EntryForm(data=request.POST)
        if form.is_valid():
            new_entry = form.save(commit=False)
            new_entry.topic = topic
            new_entry.save()
            return redirect('Note:topic')

    return render(request, "Note/new_entry.html", {'form': form, 'topic': topic})

@login_required
def edit_entry(request, entry_id):
    entry = Entry.objects.get(id=entry_id)
    topic = entry.topic

    if request.method != "POST":
        form = EntryForm(instance=entry)
    else:
        form = EntryForm(instance=entry, data=request.POST)
        if form.is_valid():
            form.save()
            return redirect("Note:topics", topic_id=topic.id)

    context = {'entry': entry, 'topic': topic, 'form': form}
    return render(request, 'Note/edit_entry.html', context)





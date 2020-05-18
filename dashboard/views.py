import csv
import io
from django.shortcuts import render
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import UserData
import operator

# Loads the dashboard and assigns table data to variables, for use in charts
@login_required
def home(request):
    names = []
    tickets_closed = []
    calls_answered = []
    counter_queries_taken = []
    chats_taken = []
    breached_tickets = []

    queryset = UserData.objects.all()
    for userdata in queryset:
        names.append(userdata.first_name)
        tickets_closed.append(userdata.tickets_closed)
        calls_answered.append(userdata.calls_answered)
        counter_queries_taken.append(userdata.counter_queries_taken)
        chats_taken.append(userdata.chats_taken)
        breached_tickets.append(userdata.breached_tickets)

    return render(request, 'dashboard/home.html', {  # Pass variables to the dashboard
        'names': names,
        'tickets_closed': tickets_closed,
        'calls_answered': calls_answered,
        'counter_queries_taken': counter_queries_taken,
        'chats_taken': chats_taken,
        'breached_tickets': breached_tickets,
    })

# Uploads the data from the CSV file into the UserData table
@login_required
def data_upload(request):

    template = "dashboard/settings.html"
    context = {}

    if request.method == "GET":
        return render(request, template, context)

    csv_file = request.FILES['file']
    if not csv_file.name.endswith('.csv'):
        messages.warning(request, 'This is not a CSV file! Please try again and input a CSV file')
        return render(request, template, context)

    data_set = csv_file.read().decode('UTF-8')
    UserData.objects.all().delete()  # Remove previous data
    io_string = io.StringIO(data_set)
    next(io_string)  # Skip CSV header
    for column in csv.reader(io_string, delimiter=',', quotechar="|"):
        _, created = UserData.objects.update_or_create(  # Assign each column of the CSV file to the UserData table
            rank_position=column[0],
            first_name=column[1],
            calls_answered=column[2],
            tickets_closed=column[3],
            average_survey_score=column[4],
            counter_queries_taken=column[5],
            chats_taken=column[6],
            breached_tickets=column[7],
            total_score=column[8]
        )

    messages.success(request, 'File successfully uploaded! Dashboard and Leaderboard changes will now take effect')
    return render(request, template, context)


@login_required
def leaderboard(request):
    names = []
    total_score = []
    queryset = UserData.objects.all()

    for userdata in queryset:
        names.append(userdata.first_name)
        total_score.append(userdata.total_score)

    all_scores = {names[i]: total_score[i] for i in range(len(names))}  # Convert names and scores into a dictionary
    sorted_scores = sorted(all_scores.items(), key=operator.itemgetter(1))  # Sort scores by total score into a list
    winner = sorted_scores[-1]  # Last score in the list is the highest, therefore the winner
    print_winner = ', '.join(map(str, winner)) + '!'  # Convert list to a string for printing

    return render(request, 'dashboard/leaderboard.html', {
        'names': names,
        'total_score': total_score,
        'print_winner': print_winner,
    })


def help(request):
    return render(request, 'dashboard/help.html')

from django.shortcuts import render
from django.http import HttpResponse
from .forms import CSVUploadForm
from pydfs_lineup_optimizer import get_optimizer, Site, Sport

def optimize(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            sport = form.cleaned_data['sport']
            site = form.cleaned_data['site']
            num_lineups = form.cleaned_data['num_lineups']

            # Save the uploaded file to a temporary location
            csv_path = f'/tmp/{csv_file.name}'
            with open(csv_path, 'wb+') as destination:
                for chunk in csv_file.chunks():
                    destination.write(chunk)

            # Use pydfs_lineup_optimizer to generate lineups
            optimizer = get_optimizer(getattr(Site, site), getattr(Sport, sport))
            optimizer.load_players_from_csv(csv_path)
            lineups = [
                {
                    'lineup': str(lineup),
                    'players': [str(player) for player in lineup.players],
                    'fantasy_points': lineup.fantasy_points_projection,
                    'salary': lineup.salary_costs,
                }
                for lineup in optimizer.optimize(n=num_lineups)
            ]

            return render(request, 'optimizer/results.html', {'lineups': lineups})

    else:
        form = CSVUploadForm()

    return render(request, 'optimizer/optimize.html', {'form': form})


def results(request):
    """
    This is a placeholder view for the results page in case you want to access it directly.
    The actual results are dynamically rendered via the optimize view.
    """
    return HttpResponse("Results will be displayed here after optimization.")

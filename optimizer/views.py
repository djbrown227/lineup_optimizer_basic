import io
import sys
from django.shortcuts import render
from django.http import HttpResponse, FileResponse
from .forms import CSVUploadForm
from pydfs_lineup_optimizer import get_optimizer, Site, Sport, Player
import os

def optimize(request):
    if request.method == 'POST':
        form = CSVUploadForm(request.POST, request.FILES)
        if form.is_valid():
            csv_file = request.FILES['csv_file']
            sport = form.cleaned_data['sport']
            site = form.cleaned_data['site']
            num_lineups = form.cleaned_data['num_lineups']

            # Get min and max exposure values from the form
            min_exposure = request.POST.get('min_exposure', 0)
            max_exposure = request.POST.get('max_exposure', 100)

            # Convert exposure values to floats
            min_exposure = float(min_exposure)
            max_exposure = float(max_exposure)

            # Save the uploaded file to a temporary location
            csv_path = f'/tmp/{csv_file.name}'
            with open(csv_path, 'wb+') as destination:
                for chunk in csv_file.chunks():
                    destination.write(chunk)

            # Use pydfs_lineup_optimizer to generate lineups
            optimizer = get_optimizer(getattr(Site, site), getattr(Sport, sport))
            optimizer.load_players_from_csv(csv_path)

            # Set min and max exposure constraints for each player
            for player in optimizer.players:
                player.min_exposure = min_exposure / 100  # Convert to fraction
                player.max_exposure = max_exposure / 100  # Convert to fraction

            # Generate lineups
            lineups = [
                {
                    'lineup': str(lineup),
                    'players': [str(player) for player in lineup.players],
                    'fantasy_points': lineup.fantasy_points_projection,
                    'salary': lineup.salary_costs,
                }
                for lineup in optimizer.optimize(n=num_lineups)
            ]

            # Generate a CSV for download
            output_csv_path = '/tmp/optimized_lineups.csv'
            optimizer.export(output_csv_path)

            # Capture player pick statistics
            old_stdout = sys.stdout  # Save the current stdout
            new_stdout = io.StringIO()  # Create a new StringIO object to capture print statements
            sys.stdout = new_stdout  # Redirect stdout to the StringIO object

            # Print player pick statistics
            optimizer.print_statistic()

            # Capture the printed statistics from the optimizer
            player_statistics = new_stdout.getvalue()

            # Reset stdout back to normal
            sys.stdout = old_stdout

            return render(request, 'optimizer/results.html', {
                'lineups': lineups,
                'csv_download_path': output_csv_path,
                'player_statistics': player_statistics
            })

    else:
        form = CSVUploadForm()

    return render(request, 'optimizer/optimize.html', {'form': form})

def download_csv(request):
    file_path = request.GET.get('file_path')
    if file_path and os.path.exists(file_path):
        return FileResponse(open(file_path, 'rb'), as_attachment=True, filename='optimized_lineups.csv')
    return HttpResponse("File not found.", status=404)

def results(request):
    """
    This is a placeholder view for the results page in case you want to access it directly.
    The actual results are dynamically rendered via the optimize view.
    """
    return HttpResponse("Results will be displayed here after optimization.")

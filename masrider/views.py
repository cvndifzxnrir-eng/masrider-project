from django.shortcuts import render, get_object_or_404, redirect
from django.contrib import messages
from django.db.models import Q, Count
from .models import MasRider, CompetitionHistory, Ability
from .forms import MasRiderForm, CompetitionHistoryForm, AbilityForm


def home(request):
    riders = MasRider.objects.annotate(
        competition_count=Count('competitions')
    )
    stats = {
        'total': riders.count(),
        'showa': riders.filter(series='showa').count(),
        'heisei': riders.filter(series='heisei').count(),
        'reiwa': riders.filter(series='reiwa').count(),
    }
    recent = riders.order_by('-created_at')[:4]
    return render(request, 'masrider/home.html', {'stats': stats, 'recent_riders': recent})


def rider_list(request):
    query = request.GET.get('q', '')
    series = request.GET.get('series', '')
    riders = MasRider.objects.annotate(competition_count=Count('competitions'))

    if query:
        riders = riders.filter(
            Q(name__icontains=query) |
            Q(alias__icontains=query) |
            Q(organization__icontains=query)
        )
    if series:
        riders = riders.filter(series=series)

    return render(request, 'masrider/rider_list.html', {
        'riders': riders,
        'query': query,
        'selected_series': series,
    })


def rider_detail(request, pk):
    rider = get_object_or_404(MasRider, pk=pk)
    competitions = rider.competitions.all()
    abilities = rider.special_abilities.all()
    wins = competitions.filter(result='win').count()
    losses = competitions.filter(result='lose').count()
    draws = competitions.filter(result='draw').count()
    return render(request, 'masrider/rider_detail.html', {
        'rider': rider,
        'competitions': competitions,
        'abilities': abilities,
        'wins': wins, 'losses': losses, 'draws': draws,
    })


def rider_create(request):
    if request.method == 'POST':
        form = MasRiderForm(request.POST)
        if form.is_valid():
            rider = form.save()
            messages.success(request, f'เพิ่มข้อมูล {rider} เรียบร้อยแล้ว!')
            return redirect('rider_detail', pk=rider.pk)
    else:
        form = MasRiderForm()
    return render(request, 'masrider/rider_form.html', {'form': form, 'action': 'เพิ่ม'})


def rider_update(request, pk):
    rider = get_object_or_404(MasRider, pk=pk)
    if request.method == 'POST':
        form = MasRiderForm(request.POST, instance=rider)
        if form.is_valid():
            form.save()
            messages.success(request, f'แก้ไขข้อมูล {rider} เรียบร้อยแล้ว!')
            return redirect('rider_detail', pk=rider.pk)
    else:
        form = MasRiderForm(instance=rider)
    return render(request, 'masrider/rider_form.html', {'form': form, 'action': 'แก้ไข', 'rider': rider})


def rider_delete(request, pk):
    rider = get_object_or_404(MasRider, pk=pk)
    if request.method == 'POST':
        name = str(rider)
        rider.delete()
        messages.success(request, f'ลบข้อมูล {name} เรียบร้อยแล้ว!')
        return redirect('rider_list')
    return render(request, 'masrider/rider_confirm_delete.html', {'rider': rider})


def competition_add(request, rider_pk):
    rider = get_object_or_404(MasRider, pk=rider_pk)
    if request.method == 'POST':
        form = CompetitionHistoryForm(request.POST)
        if form.is_valid():
            comp = form.save(commit=False)
            comp.rider = rider
            comp.save()
            messages.success(request, 'เพิ่มประวัติการต่อสู้เรียบร้อยแล้ว!')
            return redirect('rider_detail', pk=rider_pk)
    else:
        form = CompetitionHistoryForm()
    return render(request, 'masrider/competition_form.html', {'form': form, 'rider': rider})


def competition_delete(request, pk):
    comp = get_object_or_404(CompetitionHistory, pk=pk)
    rider_pk = comp.rider.pk
    if request.method == 'POST':
        comp.delete()
        messages.success(request, 'ลบประวัติการต่อสู้เรียบร้อยแล้ว!')
        return redirect('rider_detail', pk=rider_pk)
    return render(request, 'masrider/competition_confirm_delete.html', {'comp': comp})


def ability_add(request, rider_pk):
    rider = get_object_or_404(MasRider, pk=rider_pk)
    if request.method == 'POST':
        form = AbilityForm(request.POST)
        if form.is_valid():
            ability = form.save(commit=False)
            ability.rider = rider
            ability.save()
            messages.success(request, 'เพิ่มความสามารถเรียบร้อยแล้ว!')
            return redirect('rider_detail', pk=rider_pk)
    else:
        form = AbilityForm()
    return render(request, 'masrider/ability_form.html', {'form': form, 'rider': rider})

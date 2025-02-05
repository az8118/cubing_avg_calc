"""
This python script is designed to calculate the best and current Ao5, Ao12, Ao50, Ao100, Ao250, Ao500, Ao1000 and Ao2000 from a given csv file
"""
import csv

def main():
    # getting time and date in an array to work with them later
    data = [] # [[time, date], [time, date]]

    with open("CubeTime - 3x3.csv", "r", encoding="utf-8") as datei:
        reader = csv.reader(datei)
        next(reader) # skips the header line

        for line in reader:
            time, comment, scramble, date = line
            data.append([time[:6], date[:19]]) # formatieren, um unnötige informationen nicht mit reinzunehmen
    datei.close()

    data = sort_by_date(data)
    # printing results
    print(f"total solves: {len(data)}\n"
        f"Avg: current avg | best avg\n"
        f"{'-'*27}\n"
        f"Ao5:     {calc_avg(data, 5)}s | {best_avg(data, 5)}s\n"
        f"Ao12:    {calc_avg(data, 12)}s | {best_avg(data, 12)}s\n"
        f"Ao50:    {calc_avg(data, 50)}s | {best_avg(data, 50)}s\n"
        f"Ao100:   {calc_avg(data, 100)}s | {best_avg(data, 100)}s\n"
        f"Ao250:   {calc_avg(data, 250)}s | {best_avg(data, 250)}s\n"
        f"Ao500:   {calc_avg(data, 500)}s | {best_avg(data, 500)}s\n"
        f"Ao1000:  {calc_avg(data, 1000)}s | {best_avg(data, 1000)}s\n"
        f"Ao2000:  {calc_avg(data, 2000)}s | {best_avg(data, 2000)}s")

def sort_by_date(array):
    """
    sorts a given array by date trough QuickSort
    """
    if len(array) <= 1:
        return array

    pivot = array[0] 
    smaller = [i for i in array if i[1] > pivot[1]]
    middle = [i for i in array if i[1] == pivot[1]]
    bigger = [i for i in array if i[1] < pivot[1]]

    return sort_by_date(smaller) + middle + sort_by_date(bigger)

def sort_by_time(array):
    """
    sorts a given array by time trough QuickSort
    """
    if len(array) <= 1:
        return array

    pivot = array[0] 
    smaller = [i for i in array if float(i[0]) > float(pivot[0])]
    middle = [i for i in array if float(i[0]) == float(pivot[0])]
    bigger = [i for i in array if float(i[0]) < float(pivot[0])]

    return sort_by_time(smaller) + middle + sort_by_time(bigger)

def calc_avg(array, size=5):
    """
    calculating a cubing avg of a given size, e.g. Ao5 (Average of 5)
    """
    array = sort_by_time(array[0:size])
    trim = round(size * 0.05)
    if trim < 1:
        trim = 1
    times = [float(time[0]) for time in array[trim:size-trim]]
    avg = sum(times) / (size - 2*trim)
    return round(avg, 3)

# besten avg berechnen, ka wie ist von ChatGPT
def best_avg(array, size=5):
    """
    Berechnet den besten Durchschnitt für eine gegebene Anzahl an Durchläufen
    (z.B. Ao5, Ao12, etc.) mit der Sliding-Window-Technik und dem Trimmen der besten
    und schlechtesten Werte.
    """
    best_avg = float('inf')
    times = [float(i[0]) for i in array]
    
    # Berechne den ersten Durchschnitt für das erste Fenster
    for i in range(len(times) - size + 1):
        window = times[i:i+size]
        
        # Trimmen der besten und schlechtesten 5% Werte, aber nicht mehr als 1 Wert bei kleinen Fenstergrößen
        trim_size = round(size * 0.05)
        if trim_size < 1:
            trim_size = 1

        trimmed = sorted(window)[trim_size: -trim_size]
        
        # Verhindern, dass der Durchschnitt mit einem leeren Array berechnet wird
        if len(trimmed) > 0:
            avg = sum(trimmed) / len(trimmed)
            best_avg = min(best_avg, avg)
    
    return round(best_avg, 3)

if __name__ == "__main__":
    main()

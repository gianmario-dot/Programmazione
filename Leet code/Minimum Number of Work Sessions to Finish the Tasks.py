#Input: 
tasks = [3,1,3,1,1]
sessionTime = 8

#Output: 2

def minSessions(tasks, sessionTime):
    tasks.sort(reverse=True)
    sessioni = []
    
    def prova_incastri(i):
        if i == len(tasks):
            return len(sessioni)
        
        minimo_sessioni = float('inf')
        
        for j in range(len(sessioni)):
            if sessioni[j] + tasks[i] <= sessionTime:
                sessioni[j] += tasks[i]
                minimo_sessioni = min(minimo_sessioni, prova_incastri(i + 1))
                sessioni[j] -= tasks[i]
        
        sessioni.append(tasks[i])
        minimo_sessioni = min(minimo_sessioni, prova_incastri(i + 1))
        sessioni.pop()
        
        return minimo_sessioni

    return prova_incastri(0)


p=minSessions(tasks, sessionTime)
print(p)
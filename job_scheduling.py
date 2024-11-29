def job_scheduling(jobs, deadlines, profits):
    """
    Solves the Job Scheduling problem using Greedy approach.
    Schedules jobs to maximize profit while meeting deadlines.
    
    Args:
        jobs (list): List of job names/IDs
        deadlines (list): List of job deadlines
        profits (list): List of job profits
    
    Returns:
        tuple: (maximum profit achievable, list of scheduled jobs)
    """
    n = len(jobs)
    # Combine all job information and sort by profit in descending order
    job_info = list(zip(jobs, deadlines, profits))
    job_info.sort(key=lambda x: x[2], reverse=True)
    
    # Find maximum deadline to determine timeline length
    max_deadline = max(deadlines)
    # Initialize timeline slots as empty (-1)
    slot = [-1] * max_deadline
    
    total_profit = 0
    scheduled_jobs = []
    
    # Try to schedule each job as late as possible before its deadline
    for job, deadline, profit in job_info:
        # Look for available slot from deadline backwards
        for j in range(min(max_deadline, deadline)-1, -1, -1):
            if slot[j] == -1:  # If slot is empty
                slot[j] = job  # Schedule job
                total_profit += profit
                scheduled_jobs.append(job)
                break  # Move to next job
    
    return total_profit, scheduled_jobs

# Test the implementation
if __name__ == "__main__":
    # Example problem:
    # Jobs: Job1, Job2, Job3
    # Deadlines: 2, 1, 2
    # Profits: 100, 50, 200
    
    jobs = ["Job1", "Job2", "Job3"]
    deadlines = [2, 1, 2]
    profits = [100, 50, 200]

    # Get maximum profit and job sequence
    max_profit, sequence = job_scheduling(jobs, deadlines, profits)
    
    # Print results
    print(f"Maximum profit: {max_profit}")
    print(f"Job sequence: {sequence}")

# Time complexity: O(n * max_deadline) where n is number of jobs
# Space complexity: O(max_deadline) for the timeline slots 
select
	hackers.hacker_id,
	hackers.name,
	sum(submax.maxScore) totalScore

from
	(select 
		hacker_id,
		challenge_id,
		max(score) maxScore

	from
		submissions

	group by challenge_id, hacker_id) as submax
	
join hackers
	on hackers.hacker_id = submax.hacker_id

group by 
	hackers.hacker_id

order by 
	totalScore desc
from typing import List

def linear_search(nums: List[int], target: int) -> int:
	result: List[int] = []
	if(nums is None):
		return -1
	for count, val in enumerate(nums):
		if val == target:
			result.append(count)
	if len(result) == 0:
		return -1
	return result


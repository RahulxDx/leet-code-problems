class Solution:
  def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
    met = []
    for i in hours:
      if i >= target:
        met.append(i)
      return len(met)

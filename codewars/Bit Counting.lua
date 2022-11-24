local sol = {}
function sol.count_bits(n)
  local binct = 0
  local rem
  if n == 0 then
      return 0
  end
  while n > 0 do
    rem = n % 2 
    if rem ==1 then
      binct=binct+1
    end
    n = math.floor(n / 2) 
  end
  return binct
end
return sol
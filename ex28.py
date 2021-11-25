i = 1; print(i, True and True) # True
i += 1; print(i, False and True) # False
i += 1; print(i, 1 == 1 and 2 == 1) # False
i += 1; print(i, "test" == "test") # True
i += 1; print(i, 1 == 1 or 2 != 1) # True
i += 1; print(i, True and 1 == 1) # True
i += 1; print(i, False and 0 != 0) # False
i += 1; print(i, True or 1 == 1) # True
i += 1; print(i, "test" == "testing") # False
i += 1; print(i, 1 != 0 and 2 == 1) # False
i += 1; print(i, "test" != "testing") # True
i += 1; print(i, "test" == 1) # False
i += 1; print(i, not (True and False)) # True
i += 1; print(i, not (1 == 1 and 0 != 1)) # False
i += 1; print(i, not (10 == 1 or 1000 == 1000)) # False
i += 1; print(i, not (1 != 10 or 3 == 4)) # False
i += 1; print(i, not ("testing" == "testing" and "Zed" == "Cool Guy")) # True
i += 1; print(i, 1 == 1 and (not ("testing" == 1 or 1 == 0))) # True
i += 1; print(i, "chunky" == "bacon" and (not (3 == 4 or 3 == 3))) # False
i += 1; print(i, 3 == 3 and (not ("testing" == "testing" or "Python" == "Fun"))) # False

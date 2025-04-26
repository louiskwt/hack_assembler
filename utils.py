def balanced(command: str) -> bool:
    st = []
    found = False
    for i in range(len(command)):
        if command[i] == "(":
            st.append(command[i])
            found = True
        else:
            if st and (st[-1] == "(" and command[i] == ")"):
                st.pop()
    return (not st) and found
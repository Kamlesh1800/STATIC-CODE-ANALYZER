import matplotlib.pyplot as plt

if issues:
    fig, ax = plt.subplots()
    ax.bar(["Issues"], [len(issues)])
    ax.set_title("Number of Issues Found")

    st.pyplot(fig)
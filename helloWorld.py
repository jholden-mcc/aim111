
import streamlit as st
import time
import random

st.title("😎 Hello, World!")
st.write("Look out Santo... this may be a hack... ya, that's right!")

if st.button("🚀 Initiate Hack"):
    status = st.empty()
    progress = st.progress(0)
    output = st.empty()

    messages = [
        "Connecting to Santo's mainframe...",
        "Bypassing firewall...",
        "Accessing secret pizza recipes...",
        "Decrypting passwords...",
        "ERROR: Too much awesomeness detected!",
        "Re-routing through the Matrix...",
        "Locating Santo...",
        "Searching for hidden bank accounts...",
        "Downloading all the memes...",
        "WARNING: Santo has been detected!",
        "Override accepted...",
        "Finalizing totally fake hack..."
    ]

    for i in range(101):
        progress.progress(i)

        if i % 5 == 0:
            message = random.choice(messages)
            status.warning(f"⚠️ {message}")
            output.code(
                "".join(
                    random.choice("01ABCDEF#$%@")
                    for _ in range(60)
                )
            )

        time.sleep(0.15)

    progress.empty()
    status.empty()
    output.empty()

    st.error("🚨 HACK COMPLETE 🚨")
    st.markdown("## 😈 YOU ARE CHRIS SANTO!")
    st.write("I know where you live! I know where you work!")
    st.write("💸 Enjoy while I drain all your funds!")
    st.write("👋 GOODBYE, SANTO!")
    st.balloons()

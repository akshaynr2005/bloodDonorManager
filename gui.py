import streamlit as st
from donorView import bloodDonorManager

# OBJECT CREATION
donor_instance = bloodDonorManager()

st.title(" Blood Donor Management System")

tab1, tab2, tab3 = st.tabs([
    "Add Donor",
    "View Donors",
    "Update Donor"
])

# ---------------- ADD DONOR ----------------

with tab1:

    st.header("Add New Donor")

    name = st.text_input("Enter your name")
    phone = st.text_input("Enter your number")

    blood_group = st.selectbox(
        "Select Blood Group",
        ("A+", "A-", "B+", "B-", "O+", "O-")
    )

    city = st.text_input("Enter donor city")

    last_donation = st.date_input("Enter last donation date")

    if st.button("Submit"):

        if name and phone and city:

            try:
                donor_instance.post(
                    name=name,
                    phone=phone,
                    blood_group=blood_group,
                    city=city,
                    last_donation=last_donation
                )

                st.success("Donor added successfully!")

            except Exception as e:
                st.error(f"Error: {e}")

        else:
            st.warning("Please fill all the fields!")


# ---------------- VIEW DONORS ----------------

with tab2:

    st.header("View Blood Donor Details")

    donors = donor_instance.get()

    if donors:

        st.dataframe(
            donors,
            column_config={
                0: "ID",
                1: "Name",
                2: "Blood Group",
                3: "Phone",
                4: "City",
                5: "Last Donation"
            },
            hide_index=True,
            use_container_width=True
        )

    else:
        st.warning("No donors found!")


# ---------------- UPDATE DONOR ----------------

with tab3:

    st.header("Edit Donor Details")

    records = donor_instance.get()

    if records:

        blood_groups = [
            "A+", "A-", "B+", "B-", "o+", "O-"
        ]

        ids = [r[0] for r in records]

        selected_id = st.selectbox(
            "Select Donor ID",
            ids,
            key="update_id"
        )

        donor = donor_instance.get_object(id=selected_id)

        if donor:

            name = st.text_input(
                "Name",
                value=donor[1]
            )

            blood_group = st.selectbox(
                "Select Blood Group",
                blood_groups,
                index=blood_groups.index(donor[2]),
                key="update_group"
            )

            phone = st.text_input(
                "Enter your phone",
                value=str(donor[3])
            )

            city = st.text_input(
                "Enter your city",
                value=donor[4]
            )

            last_donation = st.date_input(
                "Last Donation Date",
                value=donor[5]
            )

            if st.button("Update"):

                status, message = donor_instance.put(
                    id=selected_id,
                    name=name,
                    blood_group=blood_group,
                    phone=phone,
                    city=city,
                    last_donation=last_donation
                )

                if status:
                    st.success(message)
                else:
                    st.error(message)

    else:
        st.warning("No donors available to update!")
            
        
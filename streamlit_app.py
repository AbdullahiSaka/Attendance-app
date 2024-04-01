import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from math import pi
import seaborn as sns

# Function to display the cover page
def cover_page():
    st.title("Knowledge-Based Decision Support System for Project Circularity")
    st.markdown("""
        This application is designed to collect insights on the adoption of circular economy principles in the building construction industry. 
        Participants are asked to rate their level of agreement with various decision-making factors (DMFs) that influence circular economy integration across different phases and aspects of construction projects.
        
        **Instructions:**
        - For each DMF, select your level of agreement from 1 to 5, where 1 indicates strong disagreement and 5 indicates strong agreement.
        - Your responses will help in understanding the current trends and challenges in implementing circular economy practices in the construction sector.
    """)

# Define action plans for each DMF and level of agreement
action_plans = {
    "DMF1": {
        1: "Review material procurement processes for minor improvements, such as reducing packaging waste, increasing recycled content, and avoiding over-ordering.",
        2: "Develop sustainable supplier partnerships, such as engaging with suppliers on their environmental performance, sourcing locally and ethically, and promoting circularity in the supply chain.",
        3: "Implement a comprehensive sustainable material procurement policy, such as setting clear targets and criteria for material selection, monitoring and reporting on material use and impacts, and adopting circular procurement practices such as leasing, sharing, and remanufacturing."
    },
    "DMF2": {
        1: "Encourage worker feedback on site waste management, such as soliciting suggestions for waste reduction, reuse, and recycling, and rewarding good practices.",
        2: "Train teams in advanced CE practices, such as providing education and awareness on CE principles and benefits, developing skills and competencies for CE implementation, and fostering a culture of innovation and collaboration.",
        3: "Establish guidelines for minimizing waste during construction, such as applying lean construction methods, optimizing design and prefabrication, and implementing waste hierarchy and circularity principles."
    },
    
    "DMF6": {
        1: "Implement basic pollution control measures, such as complying with environmental standards and regulations, using appropriate personal protective equipment and waste management facilities, and minimizing noise and dust emissions.",
        2: "Adopt green site practices and materials, such as reducing energy and water consumption, using renewable and low-carbon sources, and selecting eco-friendly and biodegradable materials.",
        3: "Develop a robust plan to minimize environmental impact, such as conducting a life cycle assessment, setting and monitoring environmental indicators and targets, and implementing mitigation and compensation measures."
    },
    "DMF7": {
        1: "Encourage use of eco-friendly materials in small projects, such as experimenting with alternative and innovative materials, testing their performance and feasibility, and evaluating their environmental and economic benefits.",
        2: "Implement green construction techniques broadly, such as using natural and renewable materials, applying passive design and biophilic principles, and enhancing biodiversity and ecosystem services.",
        3: "Institutionalize eco-friendly construction practices across all projects, such as establishing a green building certification system, creating incentives and rewards for green construction, and promoting green building standards and guidelines."
    },
    
    "DMF8": {
        1: "Conduct audits to identify resource inefficiencies, such as measuring and analyzing resource consumption and waste generation, identifying areas for improvement, and benchmarking against industry best practices.",
        2: "Optimize resource use in specific project areas, such as implementing resource-saving measures, applying resource-efficient technologies and processes, and achieving resource productivity and performance goals.",
        3: "Implement circularity and resource efficiency in all operations, such as adopting a circular business model, creating closed-loop systems and cycles, and maximizing resource value and utilization."
    },
   
    "DMF10": {
        1: "Assess ecological footprints in select projects, such as calculating and reporting the environmental impacts of the projects, identifying the main drivers and contributors of the impacts, and comparing the results with industry averages and benchmarks.",
        2: "Expand ecological footprint assessments to more projects, such as applying a consistent and comprehensive methodology, covering all project phases and aspects, and using the results for decision making and improvement.",
        3: "Integrate ecological footprint reduction in strategic planning, such as setting and communicating ecological footprint reduction targets and indicators, implementing and monitoring ecological footprint reduction measures and actions, and evaluating and reporting the progress and achievements."
    },
    "DMF11": {
        1: "Ensure basic compliance with CE-related policies, such as understanding and following the relevant laws and regulations, meeting the minimum requirements and standards, and avoiding penalties and sanctions.",
        2: "Engage with policymakers on CE requirements, such as providing feedback and suggestions, participating in consultations and dialogues, and advocating for favorable and supportive policies.",
        3: "Lead industry efforts in shaping and exceeding CE regulations, such as collaborating with policymakers and other stakeholders, setting and promoting best practices and voluntary commitments, and influencing and inspiring others to adopt CE."
    },
   
    "DMF14": {
        1: "Align some business strategies with CE principles, such as incorporating CE aspects into the vision and mission statements, identifying CE opportunities and challenges, and aligning CE with the core competencies and values.",
        2: "Develop CE-driven business and regulatory models, such as designing products and services for circularity, creating value propositions and revenue streams based on CE, and complying with CE-related policies and regulations.",
        3: "Fully integrate CE into business strategy and comply with regulations, such as embedding CE into the strategic objectives and goals, implementing and monitoring CE performance and outcomes, and achieving competitive advantage and leadership in CE."
    },
   
    "DMF16": {
        1: "Explore circular business models in pilot projects, such as testing and validating different circular business models, evaluating their feasibility and viability, and learning from the results and feedback.",
        2: "Develop and test circular business models, such as selecting and scaling up the most promising circular business models, refining and improving their design and delivery, and measuring and reporting their impacts and benefits.",
        3: "Fully integrate circular business models into company operations, such as adopting circular business models as the main or dominant mode of operation, creating a circular value proposition and customer base, and achieving circularity and profitability."
    },
    "DMF17": {
        1: "Initiate discussions on CE with key suppliers, such as identifying and contacting the most relevant and influential suppliers, sharing information and expectations on CE, and exploring possibilities and opportunities for collaboration.",
        2: "Develop supply chain partnerships for CE, such as establishing formal and long-term agreements and contracts with suppliers, co-creating and co-delivering CE solutions and value, and monitoring and evaluating the performance and outcomes of the partnerships.",
        3: "Fully integrate CE into the entire supply chain, such as extending CE principles and practices to all suppliers and subcontractors, creating a circular supply chain network and system, and maximizing the efficiency and effectiveness of the supply chain."
    },
   
    "DMF20": {
        1: "Introduce CE principles in some organizational processes, raising awareness among staff and integrating CE aspects into existing processes and functions.",
        2: "Expand the use of CE principles in major decisions, developing CE criteria for decision making and involving CE experts in the decision-making process.",
        3: "Embed CE principles across all organizational levels and processes, establishing a clear vision for CE and aligning all organizational processes with CE principles."
    },
    "DMF21": {
        1: "Provide basic CE training to the workforce, introducing the concept of CE and providing examples and case studies to enhance basic knowledge and awareness.",
        2: "Develop an advanced training program for CE skills, addressing CE skill gaps and designing a tailored training program to improve CE competencies.",
        3: "Establish a continuous learning culture for CE across the organization, supporting a learning environment for CE and encouraging the development of CE skills."
    },
    "DMF22": {
        1: "Encourage basic interest in CE among project leaders, informing and inspiring them about the value of CE and empowering them to explore CE initiatives.",
        2: "Develop specific CE goals for project managers and engineers, setting CE performance expectations and providing support for achieving these goals.",
        3: "Ensure strong commitment and active engagement in CE from all project leaders, involving them in CE strategy and fostering a sense of ownership for CE initiatives."
    },
    "DMF23": {
        1: "Provide introductory knowledge of CE strategies, explaining main CE strategies and highlighting their benefits to staff.",
        2: "Conduct workshops on various CE strategies, offering hands-on exercises and practical examples of applying CE strategies.",
        3: "Ensure deep understanding and application of diverse CE strategies, assessing and enhancing CE strategy knowledge and encouraging the use of diverse CE strategies in different contexts."
    },
   
    "DMF26": {
        1: "Promote general openness to CE adoption, inspiring staff about the potential of CE and empowering them to explore CE adoption.",
        2: "Cultivate a strong willingness to adopt CE practices, developing CE adoption criteria and involving staff in the CE adoption process.",
        3: "Create a culture of enthusiasm and readiness for CE adoption, establishing a clear vision for CE adoption and aligning organizational processes with CE adoption."
    },
   
    "DMF28": {
        1: "Encourage regular team communication on CE topics, providing communication channels for CE topics and soliciting team feedback.",
        2: "Enhance collaboration on CE initiatives, facilitating collaborative CE initiatives and involving team members in CE initiative design.",
        3: "Establish industry-leading practices in CE communication and collaboration, creating a system for CE communication and embedding CE practices in the industry."
    },
    "DMF29": {
        1: "Introduce the use of basic CE tools, explaining main CE tools and highlighting their benefits.",
        2: "Develop proficiency in specific CE tools and metrics, addressing CE tool gaps and designing a tailored training program.",
        3: "Achieve expert-level proficiency in a range of CE tools and performance metrics, updating CE tool knowledge regularly and facilitating advanced use of CE tools."
    },
    "DMF30": {
        1: "Encourage the use of modular elements in small projects, experimenting with modular components and evaluating their benefits.",
        2: "Train teams in advanced modular design techniques, addressing modular design skill gaps and designing a comprehensive training program.",
        3: "Fully integrate modular design and ease of disassembly in all projects, setting ambitious modular design targets and achieving high modular design goals."
    },
    "DMF31": {
        1: "Start using eco-friendly and biodegradable materials in select projects, experimenting with alternative materials and evaluating their benefits.",
        2: "Expand the use of eco-design principles and materials, applying passive design principles and enhancing biodiversity.",
        3: "Fully integrate eco-design and biodegradable materials in all products, establishing a comprehensive eco-design policy and creating a culture of eco-design."
    },
   
    "DMF33": {
        1: "Ensure basic product information is available for maintenance, collecting product information and making it accessible for maintenance staff.",
        2: "Develop comprehensive databases for product information and data, organizing product information in a structured way and providing detailed data on product performance.",
        3: "Lead in the industry in providing complete product lifecycle information, updating product information regularly and facilitating advanced access to product data."
    },
    "DMF34": {
        1: "Implement basic practices for material recovery and repair, segregating waste materials and inspecting and repairing products.",
        2: "Develop advanced systems for material recovery and reparability, using digital tools for material tracking and investing in technology for efficient repair.",
        3: "Set industry standards in material recovery and product reparability, collaborating with recovery and repair companies and achieving high recovery and reparability rates."
    },
    "DMF35": {
        1: "Assess the cost implications of basic CE integration, estimating costs and benefits of CE integration and managing financial resources.",
        2: "Conduct detailed analyses of lifecycle costs and CE integration, measuring lifecycle costs and benefits and using the results for decision making.",
        3: "Develop industry-leading practices in managing costs of CE integration, implementing a cost management model for CE integration and optimizing cost performance."
    },
    "DMF36": {
        1: "Define the scope of circular design in initial projects, introducing circular design concepts and defining expected outcomes for initial projects.",
        2: "Clarify and expand the circular design scope in major projects, reviewing initial projects to improve circular design for major projects.",
        3: "Set clear, comprehensive circular design objectives across all projects, establishing a vision for circular design and aligning project processes with circular design objectives."
    }
} 


# Function to display the cover page
def cover_page():
    st.title("Knowledge-Based Decision Support System for Project Circularity")
    st.markdown("""
        This application is designed to collect insights on the adoption of circular economy principles in the building construction industry. 
        Participants are asked to rate their level of agreement with various decision-making factors (DMFs) that influence circular economy integration across different phases and aspects of construction projects.
        
        **Instructions:**
        - For each DMF, select your level of agreement from 1 to 5, where 1 indicates strong disagreement and 5 indicates strong agreement.
        - Your responses will help in understanding the current trends and challenges in implementing circular economy practices in the construction sector.
                
        **What does it do?:**
        - For each DMF, select your level of agreement from 1 to 5, where 1 indicates strong disagreement and 5 indicates strong agreement.
        - Your responses will help in understanding the current trends and challenges in implementing circular economy practices in the construction sector.
    """)

# Define action plans for each DMF and level of agreement, now categorized and named according to the provided file
action_plans = {
    "Phase of Integration": {
        "Material Procurement Processes": action_plans["DMF1"],
        "Site Waste Management": action_plans["DMF2"]
    },
    "Environmental Consideration": {
        "Pollution and Environmental Impact": action_plans["DMF6"],
        "Eco-Friendly Construction Practices": action_plans["DMF7"],
        "Resource Efficiency and Circularity": action_plans["DMF8"],
        "Ecological Footprints and Natural Capital": action_plans["DMF10"],
        "Policy & Regulation": action_plans["DMF11"]
    },
    "Organizational Attributes": {
        "Business Strategy and CE Compliance": action_plans["DMF14"],
        "Available Circular Business Model": action_plans["DMF16"],
        "Supply Chain Integration": action_plans["DMF17"],
        "Firm Use of CE Principles": action_plans["DMF20"],
        "Availability of Skilled and Experienced Workforce": action_plans["DMF21"]
    },
    "Project Team Capacity for CE": {
        "Project Managers' and Site Engineers’ Interest in CE": action_plans["DMF22"],
        "Project Team Understanding of Various CE Strategies": action_plans["DMF23"],
        "Willingness and Readiness of Project Team to Adopt CE": action_plans["DMF26"],
        "Communication and Collaboration Among Team": action_plans["DMF28"],
        "Project Team’s Proficiency in CE Tools and Performance Metrics": action_plans["DMF29"]
    },
    "Product Feature and Circular Design": {
        "Modular Design and Ease of Disassembly/Deconstruction": action_plans["DMF30"],
        "Eco-Design and Biodegradable Materials": action_plans["DMF31"],
        "Availability of Product Information and Data": action_plans["DMF33"],
        "Material Recovery and Reparability": action_plans["DMF34"],
        "Cost Implications of CE Integration and Lifecycle Cost Analysis": action_plans["DMF35"],
        "Circular Design Scope Clarity": action_plans["DMF36"]
    }
}

# Function to display the survey form and collect responses
def data_collection():
    st.header("Data Collection")
    total_dmf_count = sum(len(dmfs) for dmfs in action_plans.values())
    answered_dmf_count = 0  # Initialize answered DMF count

    responses = {}  # Dictionary to store user responses

    # Define brief explanations for each category
    category_explanations = {
        "Phase of Integration": "This xxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxxx.",
        "Environmental Consideration": "This category deals with the construction phase, emphasizing eco-friendly practices, resource efficiency, and regulatory compliance.",
        "Organizational Attributes": "This section addresses how business strategies, models, and supply chain integration can align with circular economy principles.",
        "Project Team Capacity for CE": "This category evaluates the project team's interest, understanding, and proficiency in circular economy strategies and tools.",
        "Product Feature and Circular Design": "Here, the focus is on product design aspects such as modularity, eco-design, and material recovery, aiming for sustainability and circularity."
    }

    for category, dmfs in action_plans.items():
        st.subheader(category)
        # Display the brief explanation for the category
        st.markdown(category_explanations.get(category, "No explanation provided."))
        
        for dmf_name, levels in dmfs.items():
            response = st.selectbox(f"{dmf_name} - Select your level of agreement", options=["Select", 1, 2, 3, 4, 5], key=dmf_name)
            if response != "Select":
                responses[dmf_name] = response
                answered_dmf_count += 1  # Increment count for each answered DMF

    # Update progress after responses have been collected
    progress = answered_dmf_count / total_dmf_count
    st.progress(progress)

    if st.button("Generate Report"):
        st.session_state['responses'] = responses  # Store responses in session state
        st.experimental_rerun()  # Rerun the app to move to the report page


# Function to generate and display the report based on user responses
def generate_report():
    st.title("Report")

    # Custom CSS to style the report sections and font colors
    st.markdown("""
    <style>
    .report-section {
        border: 2px solid #4a4a4a;
        border-radius: 5px;
        padding: 20px;
        margin: 10px 0px;
    }
    .report-title {
        text-align: center;
        font-weight: bold;
        color: #3333cc; /* Dark blue color for titles */
    }
    .report-text {
        color: #666666; /* Gray color for body text */
    }
    .stTable > div > div > div > div {
        color: #004d00; /* Dark green color for table text */
    }
    </style>
    """, unsafe_allow_html=True)

    responses = st.session_state.get('responses', {})

    if not responses:
        st.error("No responses found. Please complete the survey form first.")
        return

    # Report Introduction Section with colored font
    st.markdown("""
    <div class="report-section">
        <p class="report-text">This report provides a summary of the circular economy integration levels across different categories based on the responses collected. It aims to offer insights into the current practices and areas for improvement in adopting circular economy principles within projects.</p>
    </div>
    """, unsafe_allow_html=True)

    # Calculate average values for each category
    category_averages = {}
    for category, dmfs in action_plans.items():
        category_responses = [responses[dmf_name] for dmf_name in dmfs.keys() if dmf_name in responses]
        if category_responses:
            category_averages[category] = np.mean(category_responses)

       # Calculate the Circularity Index (CI)
    CI = (category_averages.get("Phase of Integration", 0) * 0.199 +
          category_averages.get("Environmental Consideration", 0) * 0.199 +
          category_averages.get("Organizational Attributes", 0) * 0.199 +
          category_averages.get("Project Team Capacity for CE", 0) * 0.200 +
          category_averages.get("Product Feature and Circular Design", 0) * 0.204)

    # Display the averages and CI in a table
    averages_df = pd.DataFrame.from_dict(category_averages, orient='index', columns=['Average Value'])
    averages_df.loc['Circularity Index (CI)'] = CI
    st.table(averages_df)

 

    # Radar Chart Visualization Section
    st.markdown("<div class='report-section'>", unsafe_allow_html=True)
    st.markdown("<div class='report-title'>Circular Economy Integration Levels Radar Chart</div>", unsafe_allow_html=True)


    # Create a DataFrame for the radar chart
    categories = list(category_averages.keys())
    N = len(categories)

    # Compute the angle for each category
    angles = [n / float(N) * 2 * pi for n in range(N)]
    angles += angles[:1]  # Completing the circle by adding the first angle at the end

    # Initialize the radar chart
    fig, ax = plt.subplots(figsize=(6, 6), subplot_kw=dict(polar=True))

    # Draw one axe per category + add labels
    plt.xticks(angles[:-1], categories, color='grey', size=10)

    # Draw ylabels
    ax.set_rlabel_position(0)
    plt.yticks([1,2,3,4,5], ["1","2","3","4","5"], color="grey", size=7)
    plt.ylim(0,5)

    # Plot data
    values = list(category_averages.values())
    values += values[:1]  # Completing the circle
    ax.plot(angles, values, linewidth=1, linestyle='solid', label="Average Agreement")

    # Fill area
    ax.fill(angles, values, 'b', alpha=0.1)

    
    st.pyplot(fig)
    st.markdown("</div>", unsafe_allow_html=True)


    
    report_data = []

    for category, dmfs in action_plans.items():
        for dmf_name, levels in dmfs.items():
            response = responses.get(dmf_name)
            if response:
                # Retrieve the action plan for the given response, defaulting to a message if the response level isn't covered
                action_plan = levels.get(response, "No action plan available for this response level.")
                report_data.append({"DMF": dmf_name, "Response": response, "Action Plan": action_plan})
            else:
                report_data.append({"DMF": dmf_name, "Response": "Not answered", "Action Plan": "N/A"})



    # Convert the report data into a pandas DataFrame
    report_df = pd.DataFrame(report_data)

    # Display the DataFrame as a table in Streamlit
    st.table(report_df)


# Main app function
def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Go to", ["Cover Page", "Data Collection", "Generate Report"])

    if page == "Cover Page":
        cover_page()
    elif page == "Data Collection":
        data_collection()
    elif page == "Generate Report":
        generate_report()

if __name__ == "__main__":
    main()

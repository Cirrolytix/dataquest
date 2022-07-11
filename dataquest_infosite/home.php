<?php

function showHome() {
?>
    <section id="home">
        <div class="spacer"></div>
        <div id="header-1" class="headers fade">
            <div class="w3-mobile w3-display-middle">
                <div class="w3-padding-small w3-center">
                <div class="w3-row w3-center w3-padding-large">
                     <h1 class="Roboto w3-text-white w3-xxxlarge"><b>Are you up for a challenge? We are now launching Dataquest!</b></h1>
                    </div>
                    <div class="w3-hide-small w3-text-white">
                        <h1 class="Roboto w3-large"> <b>Join us on August 25-26 as we create solutions relevant to migration research, data ethics, and governance! We are now accepting submissions for the Pre-Qualifying Round at our Dataquest Community. Register now to enter the hackathon!  </b></h1>
                    </div>
              
                </div>
                <br/>
                <div class="w3-center">
                    <a href="https://dataquest.opendata.org.ph/community/entry/register?target=https%3A%2F%2Fdataquest.opendata.org.ph%2Fcommunity%2F" onclick="enrollment();">
                        <div class="w3-button w3-highway-blue w3-hover-light-blue w3-round-xxlarge w3-large">Join the Hackathon</div>
                    </a>
                </div>
            </div>
        </div>
    </section>
	<section id="objectives" class="w3-padding-32 w3-white">
        <div class="w3-center w3-content w3-padding">
            <h1 class="Roboto"><b> Dataquest 2022: Gender-Responsive Labor Migration</b></h1>
			<p class = "w3-padding-16">Welcome to the first Dataquest! Dataquest is a global hackathon that aims to invite data scientists and analysts, application developers, engineers, students, and faculty to generate ideas for good governance and development through data and technology for application in Labor Migration. CirroLytix, in partnership with UN Women, International Labor Organization, International Organization for Migration and Data Ethics PH, is holding Dataquest 2022: Gender-Responsive Labor Migration for this year's pilot run of the hackathon. </p>
            <div class="w3-center">
                    <a href="./?page=about">
                        <div class="w3-button w3-highway-blue w3-hover-light-blue w3-round-xxlarge w3-large">Learn More</div>
                    </a>
                </div>
        </div>
	</section>
    <section id="themes" class="w3-padding-64 w3-highway-blue">
        <div class="w3-center">
            <h2 class="leaguespartan">₱ 50,000</h2>
			<p>in total Prizes, across 4 Themes</p>
        </div>
        <div class="w3-row">
            <a href="?page=themes#theme1" class="w3-quarter w3-padding-large w3-center">
                <img src="images/theme1_bw.jpg" style="width: 85%;" alt="Fair, ethical and gender-responsive recruitment of OFW" />
                <p class="w3-small"><i>Photo by KC Wong</i></p>
                <p class="w3-padding-medium w3-large">Fair, ethical and gender-responsive recruitment of OFW</p>
            </a>
            <a href="?page=themes#theme2" class="w3-quarter w3-padding-large w3-center">
                <img src="images/theme2_bw.jpg" style="width: 85%;" alt="Decent work in destination countries for women OFWs" />
                <p class="w3-small"><i>Photo by ILO Asia Pacific</i></p>
                <p class="w3-padding-medium w3-large">Decent work in destination countries for women OFWs</p>
            </a>
            <a href="?page=themes#theme3" class="w3-quarter w3-padding-large w3-center">
                <img src="images/theme3_bw.jpg" style="width: 85%;" alt="Sustainable and gender-responsive reintegration of returning OFWs" />
                <p class="w3-small"><i>Photo by UN Women, Staton Winter</i></p>
                <p class="w3-padding-medium w3-large">Sustainable and gender-responsive reintegration of returning OFWs </p>
            </a>
            <a href="?page=themes#theme4" class="w3-quarter w3-padding-large w3-center">
                <img src="images/theme4_bw.jpg" style="width: 85%;" alt="Making labor migration more gender-responsive post-pandemic" />
                <p class="w3-small"><i>Photo by UN Women</i></p>
                <p class="w3-padding-medium w3-large">Making labor migration more gender-responsive post-pandemic</p>
            </a>
        </div>
        <div class="w3-center">
        
			<p>Five winning teams will be selected for special awards and given a cash prize each worth <b>₱10,000</b>. </p>
        </div>
    </section>
    <section id="awards" class="w3-padding-64 w3-pale-blue">
        <div class="w3-center">
            <h2 class="leaguespartan">Awards</h2><br>
			
        </div>
        <div class="w3-row">
            
            <a href="#awards" onclick="toggle('popup-education');" class="w3-third w3-padding-large w3-center">
                <img src="images/award1.png" style="width: 85%;" alt="Best Use of Data" />
                <p class="w3-padding-medium w3-large">Best Use of Data</p>
            </a>
            <a href="#awards" onclick="toggle('popup-peace');" class="w3-third w3-padding-large w3-center">
                <img src="images/award2.png" style="width: 85%;" alt="Best Use of Data Science" />
                <p class="w3-padding-medium w3-large">Best Use of Data Science</p>
            </a>
            <a href="#awards" onclick="toggle('popup-economy');" class="w3-third w3-padding-large w3-center">
                <img src="images/award3.png" style="width: 85%;" alt="Most Relevant to Migration Labor and Governance " />
                <p class="w3-padding-medium w3-large">Most Relevant to Migration Labor and Governance </p>
            </a></div>
            <div class="w3-row">
            <a href="#awards" onclick="toggle('popup-health');" class="w3-half w3-padding-large w3-center">
                <img src="images/award4.png" style="width: 55%;" alt="Most Practical Solution" />
                <p class="w3-padding-medium w3-large">Most Practical Solution</p>
            </a>
            <a href="#awards" onclick="toggle('popup-health');" class="w3-half w3-padding-large w3-center">
                <img src="images/award5.png" style="width: 55%;" alt="Most Gender-Responsive" />
                <p class="w3-padding-medium w3-large">Most Gender-Responsive</p>
            </a>
        </div>
    </section>

    <section id="partners" class="w3-padding-32 w3-white">
        <div class="w3-center" style="padding: 0px 0px 32px;">
            <h2 class="leaguespartan">Partners</h2>
        </div>
        <div class="w3-row">
            <div class="w3-third w3-padding-large w3-center partners">
                <a href="https://www.cirrolytix.com/" target="_blank">
                    <img src="images/cirrolytix_logo_30.png" style="width: 90%;" alt="Cirrolytix" />
                </a>
            </div>
            
            <div class="w3-third w3-padding-small w3-center partners">
                <a href="https://migrationnetwork.un.org/projects/bridging-recruitment-reintegration-migration-governance-philippines-bridge" target="_blank">
                    <img src="images/bridge.png" style="width: 55%;" alt="BRIDGE" />
                </a>
            </div>
            <div class="w3-quarter w3-padding-small w3-center partners">
                <a href="https://migrationnetwork.un.org/mptf" target="_blank">
                    <img src="images/mmptf.png" style="width: 90%;" alt="MMPTF" />
                </a>
            </div>
         
        </div>
         
        <div class="w3-row w3-padding-medium">
            <div class="w3-third w3-padding-small w3-center partners">
                <a href="https://www.ilo.org/global/lang--en/index.htm" target="_blank">
                    <img src="images/ilo.png" style="width: 80%;" alt="ILO" />
                </a>
            </div>
            <div class="w3-third w3-padding-small w3-center partners">
                <a href="https://www.iom.int/" target="_blank">
                    <img src="images/IOM_Logo.png" style="width: 80%;" alt="IOM" />
                </a>
            </div>
            <div class="w3-third w3-padding-small w3-center partners">
                <a href="https://www.unwomen.org/en" target="_blank">
                    <img src="images/un_women.png" style="width: 60%;" alt="UN WOMEN" />
                </a>
            </div>
          </div>

          <div class="w3-row w3-padding-medium">
            <div class="w3-half w3-padding-small w3-center partners">
                <a href="https://ethics.ph" target="_blank">
                    <img src="images/data_ethics.png" style="width: 30%;" alt="Data Ethics PH" />
                </a>
            </div>
            <div class="w3-half w3-padding-small w3-center partners">
                <a href="https://fma.ph/" target="_blank">
                    <img src="images/fma.png" style="width: 58%;" alt="FMA" />
                </a>
            </div>
        </div> 
    </section>
    <section class="w3-padding-32 w3-dark-grey">
        <div class="w3-center">
			<script type="text/javascript"> //<![CDATA[
			var tlJsHost = ((window.location.protocol == "https:") ? "https://secure.trust-provider.com/" : "http://www.trustlogo.com/");
			document.write(unescape("%3Cscript src='" + tlJsHost + "trustlogo/javascript/trustlogo.js' type='text/javascript'%3E%3C/script%3E"));
			//]]></script>
			<script language="JavaScript" type="text/javascript">
			TrustLogo("https://www.positivessl.com/images/seals/positivessl_trust_seal_sm_124x32.png", "POSDV", "none");
		</script>
		<br/><br/>
        </div>
    </section>
 
    <!-- Popups -->
    <section id="popup-education" class="w3-modal w3-hide" onclick="toggleClose('popup-education');">
        <div class="w3-modal-content">
            <div class="w3-black w3-bar">
                <div class="w3-bar-item">
                    <img src="images/barmm2_black.jpg" height=40 alt="BARMM Data Challenge" />
                </div>
            </div>
            <div id="theme-education" class="w3-padding">
                <div class="w3-row">
                    <div class="w3-col l1">
                        <img src="images/sdg_4.jpg" style="width: 100%;" alt="SDG 4" />
                    </div>
                    <div class="w3-col l11 w3-padding w3-text-white w3-small">
                        <h2 class="w3-large">How can data and technology help in achieving INCLUSIVE EDUCATION for all?</h2>
                        <p>Inclusive education is envisioned as part of the priorities for the Bangsamoro Education system led by the Ministry of Basic, Higher and Technical Education. It means that the education system shall have a broad, relevant, and inclusive system accessible to all students--whether Moro, Settlers, or IP. It shall also guarantee an equal opportunity for all. It is a public knowledge supported by data on learning outcomes that the quality of education in BARMM is not exemplary. This entails creating a safe and inclusive school environment for children with disabilities, cultural groups and other special circumstances. Conducting a needs assessment, developing clear guidelines and ensuring specialized support must be implemented to better respond to their situations.</p>
                        <p>Access to the data is important to provide relevant information for the education policy actors to improve access to quality and inclusive education opportunities for all children. There is a need to address issues on the monitoring and evaluation of special education (SPED) programs and teachers, integration of Madrasah education, review and contextualizing of curriculum specific to the region (including approaches with the ethnic groups) mapping SPED schools in all divisions, mapping of out of school children and youth. These examples and many more issues in the education sector need to be shown in an easily comprehensible way to the intended audience to help them make informed decisions (map, dashboard, interactive database, etc.).</p>
                    </div>
                </div>
            </div>
            <div class="w3-black w3-padding w3-small">&copy; 2020-2021 CirroLytix Research Services</div>
        </div>
    </section>
    <section id="popup-peace" class="w3-modal w3-hide" onclick="toggleClose('popup-peace');">
        <div class="w3-modal-content">
            <div class="w3-black w3-bar">
                <div class="w3-bar-item">
                    <img src="images/barmm2_black.jpg" height=40 alt="BARMM Data Challenge" />
                </div>
            </div>
            <div id="theme-peace" class="w3-padding">
                <div class="w3-row">
                    <div class="w3-col l1">
                        <img src="images/sdg_16.jpg" style="width: 100%;" alt="SDG 16" />
                    </div>
                    <div class="w3-col l11 w3-padding w3-text-white w3-small">
                        <h2 class="w3-large">How can data and technology help in promoting MORAL GOVERNANCE?</h2>
                        <p>Reforms in the governance structure are required in establishing moral governance. The challenge lies in the restoration of people's confidence in the new government, including its justice system. The experiences of previous autonomous governments shall pave the way for a new government that is responsive, transparent, accountable, and participative. Responsive policies and programs must be in place. Enabling the environment for participatory procedures shall promote the important role of CSOs representing various sectors.</p>
                        <p>The high expectations for the new government remain a problem. Increased access to information and transparency of government efforts must remain a priority. Honest and competent public officials shall be seated and undergo relevant capacity building training and values formation sessions. The monitoring and evaluation system must be built in every stage of the bureaucratic structure. An effective, people-centered feedback mechanism also needs to be in place to ensure government efforts are felt and relevant to the needs of its constituents. Trends in the use of technology need to be maximized to interpret moral governance to the ordinary citizen. A truly democratic governance in BARMM shall be achieved with vibrant civil society participation and citizens' support. Access to reliable data is crucial for people’s participation. All these elements are anchored to the Chief Minister’s policy direction and commitment for moral governance.</p>
                    </div>
                </div>
            </div>
            <div class="w3-black w3-padding w3-small">&copy; 2020-2021 CirroLytix Research Services</div>
        </div>
    </section>
    <section id="popup-economy" class="w3-modal w3-hide" onclick="toggleClose('popup-economy');">
        <div class="w3-modal-content">
            <div class="w3-black w3-bar">
                <div class="w3-bar-item">
                    <img src="images/barmm2_black.jpg" height=40 alt="BARMM Data Challenge" />
                </div>
            </div>
            <div id="theme-economy" class="w3-padding">
                <div class="w3-row">
                    <div class="w3-col l1">
                        <img src="images/sdg_1.jpg" style="width: 100%;" alt="SDG 1" />
                    </div>
                    <div class="w3-col l11 w3-padding w3-text-white w3-small">
                        <h2 class="w3-large">How can data and technology help in ALLEVIATING POVERTY and BOOSTING ECONOMIC DEVELOPMENT?</h2>
                        <p>The unprecedented impact of COVID-19 has taken its toll on the national economy and mostly felt in the poorest and rural areas in Mindanao. Prior to the enactment of the Bangsamoro Organic Law (BOL), BARMM's performance is the poorest in the country in terms of human development index. In 2018, its poverty incidence was 55.4% reaching a high per capita poverty threshold of PhP13,578 and per capita food threshold of PhP9,565.</p>
                        <p>As the means to alleviating poverty, ramping up efforts to boost the region's tourism and micro and small enterprises is vital to not backslide any achieved gains. Both sectors hold a significant part in the economy of Mindanao, which have boosted its economic development and provided employment and generated wealth for BARMM. To ease the impact to the supply chain and regional economy, government actors are rushing their way to actualize sound judgements to support affected sectors. There is a need to provide relevant information on providing economic opportunities and pivot towards innovative and speedy solutions to accurately respond with the new normal scenario. The agriculture sector, which remains resilient amidst the impact of COVID-19, is one of the potential segments to boost economic recovery in the region, hence a need for data-driven analysis for both agriculture and fishery industries are necessary.</p>
                    </div>
                </div>
            </div>
            <div class="w3-black w3-padding w3-small">&copy; 2020-2021 CirroLytix Research Services</div>
        </div>
    </section>
    <section id="popup-health" class="w3-modal w3-hide" onclick="toggleClose('popup-health');">
        <div class="w3-modal-content">
            <div class="w3-black w3-bar">
                <div class="w3-bar-item">
                    <img src="images/barmm2_black.jpg" height=40 alt="BARMM Data Challenge" />
                </div>
            </div>
            <div id="theme-health" class="w3-padding">
                <div class="w3-row">
                    <div class="w3-col l1">
                        <img src="images/sdg_3.jpg" style="width: 100%;" alt="SDG 3" />
                    </div>
                    <div class="w3-col l11 w3-padding w3-text-white w3-small">
                        <h2 class="w3-large">How can data and technology help in COVID-19 RESPONSE and RECOVERY?</h2>
                        <p>The regional government has put in place health and safety measures consistent with the national guidelines for the management of the spread of COVID-19. On 16 March 2020, President Rodrigo Roa Duterte signed Proclamation No. 929 Declaring a State of Public Health Emergency throughout the country for six (6) months mandating all government agencies and local government units (LGUs) to mobilize the necessary resources to undertake appropriate response aid and measures to eliminate COVID-19.</p>
                        <p>It is vital that communities at the grassroots level are informed about COVID-19. Relevant information allows them to make informed actions on how to protect their families and control its spread. Hence, available datasets on the spread of the disease and preventive measures are needed to be translated in an appealing way to ordinary citizens, considering area-specific nuances. However, much of the burden in controlling the transmission of the virus is on the shoulders of local government leaders-relying on government-initiated efforts on the conduct of quick and systematic contact tracing and wide testing. Thus, community leaders must be equipped in responding rapidly. Aside from this, innovations are vital to improve the quality of life of internally displaced persons (IDPs) in Marawi who have reported lack of health services (e.g. medical missions, medical clinics, affordable medicines) in their relocation sites. Best practices that can be replicated include barangay-based community management, relief and economic stimulus systems, and COVID-19 emergency maps.</p>
                    </div>
                </div>
            </div>
            <div class="w3-black w3-padding w3-small">&copy; 2020-2021 CirroLytix Research Services</div>
        </div>
    </section>
    
    <?php
}
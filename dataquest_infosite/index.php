<!DOCTYPE HTML>
<html lang="en">

<head>
    <title>Dataquest 2022: Gender-Responsive Labor Migration</title>
    <link rel="stylesheet" href="resources/app_css.css" />
    <link rel="stylesheet" href="resources/w3.css" />
    <link rel="stylesheet" href="https://www.w3schools.com/lib/w3-colors-highway.css">
    <link rel="shortcut icon" href="favicon.png" type="image/x-icon" />
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="title" content="Dataquest 2022: Gender-Responsive Labor Migration" />
    <meta name="description" content="Dataquest is a hackathon that brings together data scientists and analysts, engineers, application developers, students, faculty, professionals, non-profit organizations, and social enterprises to generate data-driven and technology-based solutions for reaching the UN Sustainable Development Goals and remediating society's most pressing problems." />
    <meta property="og:url" content="https://dataquest.opendata.org.ph" />
    <meta property="og:type" content="website" />
    <meta property="og:title" content="Dataquest 2022: Gender-Responsive Labor Migration" />
    <meta property="og:description" content="Dataquest is a hackathon that brings together data scientists and analysts, engineers, application developers, students, faculty, professionals, non-profit organizations, and social enterprises to generate data-driven and technology-based solutions for reaching the UN Sustainable Development Goals and remediating society's most pressing problems." />
    <meta property="og:image" content="images/dataquest_logo.png" />
	<!-- Global site tag (gtag.js) - Google Analytics -->
	<script async src="https://www.googletagmanager.com/gtag/js?id=G-HYTE8Z647C"></script>
	<script>
	  window.dataLayer = window.dataLayer || [];
	  function gtag(){dataLayer.push(arguments);}
	  gtag('js', new Date());

	  gtag('config', 'G-HYTE8Z647C');
	</script>	
</head>

<body class="Roboto">
    <header class="w3-top w3-black">
        <div class="w3-bar">
            <div class="w3-bar-item">
                <a href ="./?page=home" class= "w3-padding-large"> 
                <img src="images/dataquest_svg.svg" width=145% height=100px   alt="Dataquest" /></a>
            </div>
            <span class="w3-hide-small w3-hide-medium">
				<a href="https://dataquest.opendata.org.ph/community/entry/register?target=https%3A%2F%2Fdataquest.opendata.org.ph%2Fcommunity%2F" class="w3-bar-item w3-button w3-highway-blue w3-round-xxlarge w3-padding w3-hover-light-blue w3-margin-right w3-right" style="height: 40px; margin-top: 40px; padding: 12px;">Register Now</a>
				<a href="https://dataquest.opendata.org.ph/community/" class="w3-bar-item w3-button w3-hover-text-white w3-hover-none w3-right" style="height: 100px; padding-top: 50px;">Community</a>
				<a href="./?page=news" class="w3-bar-item w3-button w3-hover-text-white w3-hover-none w3-right" style="height: 100px; padding-top: 50px;">News</a>
				<a href="./?page=team" class="w3-bar-item w3-button w3-hover-text-white w3-hover-none w3-right" style="height: 100px; padding-top: 50px;">Meet the Team</a>
				<a href="./?page=partners" class="w3-bar-item w3-button w3-hover-text-white w3-hover-none w3-right" style="height: 100px; padding-top: 50px;">Partners</a>
				<a href="./?page=mentors-judges" class="w3-bar-item w3-button w3-hover-text-white w3-hover-none w3-right" style="height: 100px; padding-top: 50px;">Mentors & Judges</a>
				<a href="./?page=resources" class="w3-bar-item w3-button w3-hover-text-white w3-hover-none w3-right" style="height: 100px; padding-top: 50px;">Resources</a>
				<a href="./?page=themes" class="w3-bar-item w3-button w3-hover-text-white w3-hover-none w3-right" style="height: 100px; padding-top: 50px;">Themes</a>
				<a href="./?page=rules" class="w3-bar-item w3-button w3-hover-text-white w3-hover-none w3-right" style="height: 100px; padding-top: 50px;">Rules</a>
				<a href="./?page=about" class="w3-bar-item w3-button w3-hover-text-white w3-hover-none w3-right" style="height: 100px; padding-top: 50px;">About</a>
				
			</span>
    </div>
    </header>
    <div class="w3-row">

    <?php
		include ('home.php');
		include ('themes.php');
		include ('mentors-judges.php');
		include ('rules.php');
		include ('news.php');
		include ('resources.php');
		include ('team.php');
		include ('about.php');
		include ('partners.php');
		
		if (isset($_GET["page"])) {
			$page = $_GET["page"];
			switch ($page) {
				case "home":
					showHome();
					break;
				case "themes":
					showThemes();
					break;
				case "mentors-judges":
					showMentorsJudges();
					break;
				case "rules":
					showRules();
					break;
				case "news":
					showNews();
					break;
				case "resources":
					showResources();
					break;
				case "team":
					showTeam();
					break;
				case "about":
					showAbout();
					break;
				case "partners":
					showPartners();
					break;
		} 
		} else {
			showHome();
		}
		?>


    </div>









    <footer class="w3-black w3-small w3-bottom w3-bar">
        <span class="w3-hide-small">
			<div class="w3-bar-item">&copy; 2022 CirroLytix Research Services</div>
			<div onclick="toggle('privacy');" class="w3-bar-item w3-hover-text-white w3-hover-none w3-right w3-button">Privacy and Terms of Use</div>
		</span>
    </footer>

		<section id="privacy" class="w3-modal w3-hide" onclick="toggleClose('privacy');">
        <div class="w3-modal-content w3-animate-zoom ">
             <div class="w3-padding">
                <div class="w3-row">
                    <div class="w3-padding w3-small">
                        <h2>Privacy Policy</h2>
                        <p>It is our policy to respect your privacy regarding any information we may collect while operating this website. We are committed to protect personally identifiable information you may provide us through the website.</p>
                        <h3>Website Visitors</h3>
                        <p>We collect non-personally-identifying information that web browsers and servers make available, such as browser type, language preferences, referring site, and date and time of each visitor request. Our purpose for collecting this is to better understand how our visitors use our site. We may from time to time, release non-personally-identifying information in the aggregate, e.g. by publishing a report on website usage trends. </p>
                        <h3>Gathering of Personally-Identifying Information</h3>
                        <p>Certain visitors' websites choose to interact with our website in ways that require us to collect personally-identifying information. The amount and type of information that we gather depends on the nature of the transaction. We may ask visitors to sign-up for a section of the site that require a username and password.</p>
                        <h3>Security</h3>
                        <p>We strive to use commercially acceptable means to protect our user's information. We try our best to secure websites, but cannot guarantee absolute security. </p>
                        <h3>Advertisements</h3>
                        <p>Ads appearing on our site may be delivered to users by partners, who may set cookies. These cookies allow us to recognize your computer each time they send you an online advertisement to compile information about you or others who use your computer.</p>
                        <h3>Links to External Sites</h3>
                        <p>Our site may link to other sites that are not operated by us. If you click on a third party link, you will be directed to that third-party's site. Please review the privacy policy and terms of use of those sites in the event you have been redirected.</p>
                        <h3>Aggregated Statistics</h3>
                        <p>We may collect statistics about the behavior of visitors to its website. We may display information publicly or provide it to others. We do not disclose personally-identifying information.</p>
                        <h3>Cookies</h3>
                        <p>To improve the user experience, we use "Cookies", a string of information that a website stores on a visitor's computer, and that the visitor's browser provides to the website each time the visitor returns. We use cookies to help identify and track visitors, their usage of our website and their access preferences. Visitors who do not wish to have cookes placed on their computers should set their browsers to refuse cookies before using our website, with the drawback that certain features may not function properly without cookies. </p>
                        <h3>Changes to Policy</h3>
                        <p>We may change our privacy policy from time to time at our sole discretion. We encourage visitors to frequently check this page for any changes to its privacy policy. Your continued use of the site after any change in this policy will constitute your acceptance.</p>
                        <hr/>
                        <h2>Terms of Use</h2>
                        <p>These terms and conditions outline the use of our website. By accessing this site we assume you accept these terms in full. If you do not accept all of these terms, please do not continue to use our website.</p>
                        <h3>Cookies</h3>
                        <p>We use cookies on this site. By using our website you consent to the use of cookies in accordance with our <b>privacy policy</b></a>.</p>
                        <h3>License</h3>
                        <p>CirroLytix Research Services own the intellectual property rights for all material on this website and all rights are reserved. You may view and/or print pages from this website for your personal use subject to these terms and conditions.</p>
                        <p>You must not:
                            <ul>
                                <li>Republish material from this website.</li>
                                <li>Sell, rent, or sub-license material from this website.</li>
                                <li>Reproduce, duplicate, or copy material from this webiste.</li>
                                <li>Redistribute content from this website (unless content is specifically made for redistribution).</li>
                            </ul>
                        </p>
                        <h3>Hyperlinks</h3>
                        <p>The following organizations may link to our website without prior written approval:
                            <ul>
                                <li>Government agencies;</li>
                                <li>Search engines;</li>
                                <li>News organizations;</li>
                                <li>Online directories;</li>
                            </ul>
                            These organizations may link to our home page, to publications or to other website information so long as the link: (a) is not misleading; (b) does not imply sponsorship, endorsement, or approval of the linking party and its products or services; and (c) fits within the context of the linking party's site.</p>
                        <p>We may consider and approve at our discretion link requests from these organizations:
                            <ul>
                                <li>Consumer and business information sources;</li>
                                <li>Community sites;</li>
                                <li>Associations;</li>
                                <li>Internet portals;</li>
                                <li>Accounting, law, consulting firms;</li>
                                <li>Educational institutions and research companies;</li>
                            </ul>
                            We will approve link requests from these organizations if: (a) the link would not look unfavorably on us; (b) the organization does not have an unsatisfactory history with us; (c) the benefit to us from the visibility associated with the link exceeds the absence of CirroLytix Research Services; and (d) if the link is in the context of general resource information or editorial content that furthers our mission. </p>
                        <h3>Iframes</h3>
                        <p>You may not create frames around our web pages without our approval. You may not use other techniques that later in any way alter the visual presentation or appearance of our site.</p>
                        <h3>Reservation of Rights</h3>
                        <p>We reserve the right and sole discretion to request that you remove all links or a particular link to our website. You agree to immediately remove all such links upon request. We also reserve the right to amend these terms and conditions and linking policy at any time. </p>
                        <h3>Removal of Links</h3>
                        <p>If you find any link on our website to be objectionable, you may contact us about this. We will consider such requests but will have no obligation to do so or respond directly. We endeavour to ensure that all information on this site is correct, but do not warrant its completeness or accuracy; nor do we commit to ensuring that the site remains available or that the site is kept up to date.</p>
                        <h3>3rd Party Content Liability</h3>
                        <p>We shall have no liability for any content appearing on your website. You agree to indemnify and defend us against all claims rising out of or based upon your website. </p>
                        <h3>Contact Us</h3>
                        <p>For any questions on these terms, you can contact us at: <b>bridge@cirrolytix.com</b>.</p>
                    </div>
                </div>
            </div>
            <div class="w3-black w3-padding w3-small">&copy; 2020-2021 CirroLytix Research Services</div>
        </div>
    </section>
    <script src="resources/app_js.js"></script>
</body>

</html>
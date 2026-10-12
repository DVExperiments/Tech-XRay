"""Rebuild the local web-ready challenge library from curated Python content.
No dependencies, remote services, or API keys.
"""
import json
from pathlib import Path
ROOT = Path(__file__).resolve().parents[1]
# Each evidence card: claim, layer, explanatory feedback, is a high-priority dependency?
T = []
def add(id, title, field, icon, teaser, scenario, cards, blindspots):
    assert len(cards) == 12, f'{id}: expected 12 evidence cards'
    assert len(blindspots) == 3
    T.append({'id':id,'title':title,'field':field,'icon':icon,'teaser':teaser,'scenario':scenario,
              'cards':[{'id':f'{id}-{i+1}', 'text':c[0], 'layer':c[1], 'why':c[2], 'critical': bool(c[3]) if len(c)>3 else False} for i,c in enumerate(cards)],
              'blindspots':[{'title':b[0], 'explanation':b[1], 'question':b[2]} for b in blindspots]})

add('genai','Generative AI','Computing','✦',
    'Systems that generate text, images, audio or code from learned patterns.',
    'A team wants to introduce a generative AI assistant into everyday work.',[
    ('Drafts text and summarises material from prompts.','does','Generating content is a capability, although output quality varies.'),
    ('Can produce plausible but false statements.','limits','Confident errors are a limitation that calls for verification.'),
    ('Relies on model weights and computing infrastructure.','needs','Models require execution hardware and a deployed software system.',True),
    ('Workers may gain speed but face changes in tasks and expectations.','affects','The workforce experiences both potential benefits and organisational impacts.'),
    ('Requires appropriate access to input data and documents.','needs','The usefulness and risks depend on which information the model can access.',True),
    ('May assist with translation and idea generation.','does','Supporting drafting and language tasks is a possible function.'),
    ('Sensitive prompts could disclose private information.','limits','Data privacy is a constraint on safe deployment.'),
    ('Needs evaluation and human checking in consequential uses.','needs','Oversight and testing are operational requirements for dependable use.',True),
    ('Clients or learners may receive more accessible explanations.','affects','The people receiving AI-supported work can be affected.'),
    ('Can adapt the style of a response for a target audience.','does','Prompt-based tailoring is a capability.'),
    ('Depends on network connectivity for cloud-hosted models.','needs','Cloud services need connectivity, although some models can run locally.'),
    ('May inherit patterns or biases present in training data.','limits','Unequal or biased outputs are a quality and fairness limitation.')],
    [('Accountability and escalation','Someone must own mistakes, exceptions and decisions when the model is wrong.','Who can intervene or override the model?'),
     ('Data governance','Retention, consent, permitted use and access rules matter as much as the model itself.','Can you explain where prompts and outputs go?'),
     ('Ongoing maintenance','Models, policies, costs and user practices change after launch.','How will you detect performance drift or misuse?')])

add('digital-twins','Digital Twins','Systems','◎',
    'A continuously informed digital representation of a physical system or process.',
    'A city is considering a digital twin to improve how it manages infrastructure.',[
    ('Simulates what-if changes before trying them physically.','does','Scenario testing is a central potential use of a digital twin.'),
    ('Requires reliable information about the real system.','needs','A twin is only as useful as the quality of its model and data.',True),
    ('Outdated sensors can create a misleading picture.','limits','Poor data can make the representation inaccurate.'),
    ('Infrastructure operators can use it to plan maintenance.','affects','Operators are a primary stakeholder group.'),
    ('Needs a way to refresh data as conditions change.','needs','A living twin needs suitable data collection and integration.',True),
    ('Can visualise assets, flows and system behaviour.','does','Making complex system states visible is a capability.'),
    ('Building and validating detailed models takes resources.','limits','Model fidelity, cost and effort constrain adoption.'),
    ('Residents may be affected by decisions informed by it.','affects','People outside the technical team can experience downstream consequences.'),
    ('Depends on clearly defined model boundaries.','needs','A twin must specify what is represented and what is not.',True),
    ('Can flag possible asset failures from patterns in data.','does','Analysis can help anticipate problems where data and models support it.'),
    ('Requires people who can interpret and challenge outputs.','needs','Expertise is needed to use the model responsibly.'),
    ('Cannot represent every unexpected real-world event.','limits','Models are simplifications, not perfect copies of reality.')],
    [('Model ownership','Maintenance responsibility and update processes are essential after the first demonstration.','Who keeps the twin accurate next year?'),
     ('Interoperability','Data often spans vendors, formats and departments that do not communicate cleanly.','Which data systems must connect?'),
     ('Decision pathways','A useful simulation does not automatically lead to better action.','Who decides what to do with model outputs?')])

add('ar','Augmented Reality','Interfaces','◈',
    'Digital information layered into a person’s view of the physical world.',
    'An organisation wants to use augmented reality for workplace learning.',[
    ('Places visual instructions over a real task.','does','Overlaying guidance is a common AR function.'),
    ('Needs suitable screens, cameras or wearable hardware.','needs','An interface must display digital content in the user’s environment.',True),
    ('Eye strain or discomfort can interrupt use.','limits','Ergonomics affects how long and how safely people can use it.'),
    ('Learners may get contextual guidance at the point of work.','affects','The people being trained are directly affected.'),
    ('Requires a way to track position and surfaces.','needs','Registration and tracking help digital objects line up with the world.',True),
    ('Can show a 3D model at real-world scale.','does','Spatial placement is an AR capability.'),
    ('Occlusion and poor tracking can cause misalignment.','limits','Inaccurate overlays can reduce usability or trust.'),
    ('Bystanders can be affected by cameras in shared spaces.','affects','Camera-based interaction raises concerns beyond the primary user.'),
    ('Needs content designed for the specific task and environment.','needs','Context-sensitive content is essential for meaningful use.',True),
    ('Can reveal hidden components of equipment visually.','does','AR can illustrate information not directly visible.'),
    ('Depends on device power and battery life.','needs','Wearable or mobile systems need adequate power.'),
    ('Bright light, clutter or accessibility needs may limit usability.','limits','Environmental and human differences affect performance.')],
    [('Physical safety','Users need to see hazards and stay attentive to their surroundings.','Could an overlay hide a risk?'),
     ('Accessibility alternatives','Not everyone can comfortably use headsets, gestures or visual cues.','What equivalent non-AR pathway exists?'),
     ('Consent in shared spaces','Bystanders may not expect a device to capture images of them.','What is captured, stored or shared?')])

add('edge-ai','Edge AI','Computing','⌁',
    'Running AI inference near where data is produced, rather than always in a distant cloud.',
    'A manufacturer is exploring AI analysis on devices on the factory floor.',[
    ('Can analyse sensor data without sending every event to the cloud.','does','Local inference is a central capability of edge AI.'),
    ('Needs hardware powerful enough for the chosen model.','needs','Processor, memory and acceleration limit which models can run.',True),
    ('Small devices may struggle with large models.','limits','Compute, memory and energy budgets constrain performance.'),
    ('Maintenance teams may receive faster fault alerts.','affects','Operators and staff can be affected by predictions and alerts.'),
    ('Requires a model packaged for the target device.','needs','Deployment and optimisation must match hardware constraints.',True),
    ('Can reduce latency for some real-time decisions.','does','Processing nearby often shortens the network round trip.'),
    ('Different devices make updating software harder.','limits','Fleet management is an operational challenge.'),
    ('People being monitored may have privacy concerns.','affects','Sensor-based systems can affect workers or community members.'),
    ('Needs an approach for distributing secure updates.','needs','Devices must receive patches and model changes safely.',True),
    ('Can continue some functions during a network outage.','does','Local operation can reduce dependence on constant connectivity.'),
    ('Depends on sufficient sensor input quality.','needs','Poor observations cannot reliably support useful predictions.'),
    ('Offline operation does not guarantee privacy.','limits','Local devices can still log, share or leak personal data.')],
    [('Device lifecycle','A deployed device needs support long after its first software release.','How will older devices be patched?'),
     ('Physical security','Hardware in public or distributed locations can be stolen or tampered with.','What happens if someone accesses the device?'),
     ('Fallbacks','Local automated decisions still need safe behaviour when sensors or models fail.','What is the safe default when confidence is low?')])

add('robots','Autonomous Delivery Robots','Robotics','▣',
    'Mobile robots that move items through mapped or partially understood environments.',
    'A campus is considering robots to deliver supplies between buildings.',[
    ('Can move small loads with limited direct supervision.','does','Transporting goods is the robot’s intended service.'),
    ('Needs localisation, mapping and obstacle detection.','needs','Navigation requires sensing where the robot is and what is nearby.',True),
    ('Uneven paths, stairs and weather limit reliable routes.','limits','Physical environments impose practical constraints.'),
    ('Pedestrians and people using mobility aids share the space.','affects','Public users of paths can be affected, whether or not they use the service.'),
    ('Requires reliable charging and maintenance arrangements.','needs','Power and upkeep support day-to-day operation.',True),
    ('Can follow a route and adjust around obstacles.','does','Path planning and avoidance are capabilities.'),
    ('Some edge cases still require remote human help.','limits','Real-world autonomy is bounded and can need intervention.'),
    ('Delivery workers and logistics teams may see tasks change.','affects','Automation changes job workflows.'),
    ('Needs appropriate permissions to operate in its area.','needs','Site rules and applicable law shape deployment.',True),
    ('May provide predictable tracking and delivery updates.','does','Status reporting can make logistics more visible.'),
    ('Depends on a reliable way to load and receive parcels.','needs','The whole service needs hand-off processes, not just motion.'),
    ('Vandalism or blocked routes can interrupt operation.','limits','Uncontrolled environments introduce disruption.')],
    [('Inclusive route design','Routes must not block footpaths or create disproportionate accessibility barriers.','Would the robot obstruct wheelchair users?'),
     ('Human override','Staff need to recover stuck units and handle unusual incidents.','Who responds when the robot stops?'),
     ('Service economics','Purchase price is only one part of staffing, upkeep and replacement costs.','What does a full year of operation cost?')])

add('synbio','Synthetic Biology','Biotechnology','❋',
    'Engineering biological systems to perform useful functions.',
    'A team is considering engineered microbes for a new material or manufacturing process.',[
    ('Can modify organisms to produce useful molecules.','does','Engineering pathways for a desired output is a possible application.'),
    ('Requires a suitable biological host and design.','needs','The organism and engineered system must support the intended function.',True),
    ('Biological performance may change outside lab conditions.','limits','Living systems can behave differently across environments.'),
    ('Communities may have concerns about environmental release.','affects','People in affected areas have legitimate stakes in decisions.'),
    ('Needs controlled testing and validated measurements.','needs','Evidence of performance and safety depends on good experiments.',True),
    ('Can support new enzymes, materials or production methods.','does','Biological manufacturing is a potential capability.'),
    ('Scaling from a lab to a factory can be difficult.','limits','Industrial conditions introduce yield and cost challenges.'),
    ('Workers may require new laboratory and safety skills.','affects','Operational roles and training requirements can change.'),
    ('Depends on appropriate biosafety controls and governance.','needs','Containment, oversight and rules are part of responsible use.',True),
    ('Can make some production processes more targeted.','does','Designed organisms can carry out specific transformations.'),
    ('Needs nutrients, equipment and reliable process conditions.','needs','Biological production depends on a stable operating environment.'),
    ('Unintended biological effects require evaluation.','limits','Complex biological interactions create uncertainty.')],
    [('Life-cycle impact','A biological process is not automatically lower-impact once inputs and waste are counted.','What energy, feedstocks and disposal routes are involved?'),
     ('Community engagement','A project can affect groups whose views differ from the technical team’s.','Who should shape the project before trials?'),
     ('Containment and recovery','Responsible deployment must account for unexpected escape or process failure.','What happens if containment fails?')])

add('quantum','Quantum Computing','Computing','✳',
    'Computing systems that manipulate quantum information rather than only classical bits.',
    'An organisation is evaluating whether quantum computing could help with complex problems.',[
    ('May accelerate certain specialised algorithms.','does','Quantum advantage is problem- and method-dependent, not universal.'),
    ('Needs high-quality qubits and precise control systems.','needs','Useful computation depends on quantum hardware and control.',True),
    ('Qubits are susceptible to noise and errors.','limits','Noise is a major barrier to reliable long calculations.'),
    ('Researchers and specialised technical teams may benefit first.','affects','Early adoption tends to involve organisations with relevant expertise.'),
    ('Requires suitable algorithms for the target problem.','needs','A quantum device is not automatically useful for every workload.',True),
    ('Can explore quantum systems through simulation techniques.','does','Modelling quantum behaviour is an important potential use case.'),
    ('Fault-tolerant, large-scale capabilities remain difficult.','limits','Present systems have limitations and should not be oversold.'),
    ('Cybersecurity teams must plan for future cryptographic risks.','affects','Long-term cryptographic transition planning affects institutions.'),
    ('Needs error-management and calibration strategies.','needs','Maintaining useful calculations requires active error mitigation or correction.',True),
    ('Uses superposition and entanglement as computational resources.','does','These quantum properties underpin classes of algorithms.'),
    ('Some hardware designs require extreme cooling or vacuum systems.','needs','Physical requirements vary by qubit technology.'),
    ('Does not simply make all conventional computers obsolete.','limits','Quantum devices are specialised tools, not general-purpose replacements.')],
    [('Benchmark fairness','Quantum claims should be compared against strong classical baselines.','Which classical method was the benchmark?'),
     ('Hybrid workflows','Quantum and classical computing often need to work together.','Where does the quantum step sit in the full task?'),
     ('Skills and access','Access to devices and people who understand them can be a major bottleneck.','Who can validate and use the result?')])

add('hydrogen','Green Hydrogen','Energy','◉',
    'Hydrogen produced through electrolysis powered by low-emissions electricity.',
    'A region is exploring green hydrogen for industrial use or transport.',[
    ('Can provide a fuel or feedstock for selected applications.','does','Hydrogen can supply chemical and energy services.'),
    ('Needs electricity and water to run electrolysers.','needs','Electrolysis splits water using electrical energy.',True),
    ('Energy losses occur in production, storage and use.','limits','Conversion steps reduce the efficiency of the full pathway.'),
    ('Industrial workers and nearby communities may be affected.','affects','New facilities change local jobs and infrastructure.'),
    ('Requires suitable storage and transport infrastructure.','needs','Hydrogen handling needs purpose-built systems and controls.',True),
    ('Could replace some fossil-derived hydrogen in industry.','does','Substitution in existing industrial demand is a credible use.'),
    ('High costs can limit commercial competitiveness.','limits','Costs depend on electricity, equipment and utilisation.'),
    ('Electricity users may compete for low-emissions power.','affects','Energy allocation can have broader system consequences.'),
    ('Needs safety procedures for a highly flammable gas.','needs','Safe storage, ventilation and leak detection are crucial.',True),
    ('Can store energy for later conversion, with losses.','does','Energy storage is possible but not always the most efficient use.'),
    ('Depends on credible assessment of electricity emissions.','needs','Environmental claims depend on how the power is generated.'),
    ('Is unlikely to be the best option for every energy need.','limits','Direct electrification may be more efficient in many cases.')],
    [('Opportunity cost of power','Limited clean electricity could instead directly decarbonise other activities.','What use of the electricity gives the best outcome?'),
     ('Water and place','Water sourcing and local ecology need assessment in context.','Who else relies on this water source?'),
     ('End-to-end carbon accounting','Production labels alone may hide transport, leakage and energy-system emissions.','Where are the system boundaries for the carbon claim?')])

add('bioprint','3D Bioprinting','Biotechnology','▥',
    'Layer-by-layer deposition of cells and biomaterials to form tissue-like structures.',
    'A research group is exploring printed tissue models for drug development.',[
    ('Can create structured tissue models for laboratory research.','does','Producing tissue-like models is a current research application.'),
    ('Needs suitable cells, biomaterials and printing equipment.','needs','Living structures depend on viable biological inputs and tools.',True),
    ('Keeping thick tissues alive can be difficult.','limits','Nutrient delivery and vascularisation remain major challenges.'),
    ('Researchers may use models to study disease or drug effects.','affects','Research teams and, indirectly, patients are stakeholders.'),
    ('Requires sterile processes and careful environmental control.','needs','Cell survival and contamination control depend on conditions.',True),
    ('Can control where different materials and cells are deposited.','does','Spatial placement is a defining technique.'),
    ('Printed structures may not behave like real organs.','limits','Biological fidelity and function are not guaranteed.'),
    ('Patients may be affected by future clinical claims and choices.','affects','The claims and expectations around research affect the public.'),
    ('Needs testing of cell viability and tissue function.','needs','Printed appearance alone does not demonstrate biological usefulness.',True),
    ('May reduce reliance on some animal models in specific research.','does','Better laboratory models could replace some experiments, case by case.'),
    ('Depends on design files and reproducible print settings.','needs','Repeatability requires controlled instructions and parameters.'),
    ('Printing transplant-ready organs is not a routine clinical service.','limits','The leap from models to fully functional transplant organs is substantial.')],
    [('Clinical translation','Regulatory evidence and long-term safety would be required before medical use.','What would need proving before use with a patient?'),
     ('Ethical cell sourcing','Consent and provenance of biological samples matter.','Where did the cells come from and with what permission?'),
     ('Reproducibility','Small variations can change biological results between laboratories.','Can another team reproduce the tissue properties?')])

add('smart-grid','Smart Grids','Energy','⊞',
    'Electricity networks using digital sensing and control to manage changing supply and demand.',
    'A council is considering smart-grid upgrades for a growing community.',[
    ('Can improve visibility of electricity demand and network conditions.','does','Network sensing and analysis help operators observe change.'),
    ('Needs connected meters, sensors and control equipment.','needs','Digital monitoring requires instrumentation.',True),
    ('Cyberattacks or network outages can disrupt operations.','limits','Connectivity adds new failure and security considerations.'),
    ('Households may get new ways to understand energy use.','affects','Customers can be affected by smart meters or pricing signals.'),
    ('Requires reliable communication between network components.','needs','Data and control signals must reach the right systems.',True),
    ('Can help coordinate distributed solar and batteries.','does','Managing two-way flows is an important capability.'),
    ('Legacy equipment can be expensive to integrate.','limits','Old infrastructure may not support modern digital interfaces.'),
    ('Electricity network operators may change working practices.','affects','Operating teams need new tools, skills and decisions.'),
    ('Needs clear safety rules and fallback operation.','needs','Grid reliability depends on safe behaviour during errors.',True),
    ('May shift flexible consumption away from peak periods.','does','Demand response can help manage peaks when appropriately designed.'),
    ('Depends on good data handling and access controls.','needs','Fine-grained use data deserves appropriate protection.'),
    ('Benefits may be uneven for people without flexible appliances.','limits','Not every customer can respond to pricing or automation.')],
    [('Equity in incentives','Price schemes may disadvantage those unable to shift their energy demand.','Who can and cannot benefit from the programme?'),
     ('Operational fallback','Manual procedures must still work if digital coordination fails.','What happens when communication is lost?'),
     ('Community trust','Smart-meter data may reveal routines and raise concerns.','How are consumers informed and involved?')])

add('satellite','Satellite Internet','Infrastructure','◇',
    'Connectivity delivered through satellites and user terminals, including low-Earth-orbit systems.',
    'A remote community is weighing satellite internet as an option for connectivity.',[
    ('Can deliver broadband to some areas without terrestrial fibre.','does','Satellites can extend access where fixed networks are hard to reach.'),
    ('Needs a compatible user terminal and suitable sky view.','needs','Users need ground equipment with an appropriate link.',True),
    ('Weather, obstacles or congestion can affect the service.','limits','Coverage and performance vary by environment and capacity.'),
    ('Rural residents may gain new remote-learning opportunities.','affects','People with limited existing internet are key stakeholders.'),
    ('Requires a functioning satellite constellation or network.','needs','The service depends on orbital infrastructure.',True),
    ('Can support communication after some terrestrial failures.','does','Alternative paths can aid resilience in some disasters.'),
    ('Affordability and power needs may block access.','limits','Equipment, subscriptions and energy cost money.'),
    ('Astronomers can be affected by the growing number of satellites.','affects','Night-sky observation and the space environment are affected.'),
    ('Needs ground gateways and wider internet connections.','needs','Satellites must connect users to broader networks.',True),
    ('Enables mobile connectivity in suitable circumstances.','does','Some services support moving vehicles or remote sites.'),
    ('Depends on spectrum allocation and regulatory permissions.','needs','Radio operation and coverage are subject to applicable rules.'),
    ('Space debris and network congestion create external costs.','limits','Scaling large constellations brings orbital and radio challenges.')],
    [('Local support','Equipment failures are harder to resolve where technicians are far away.','Who can maintain the terminal locally?'),
     ('Resilience assumptions','An outage in power or ground infrastructure can interrupt satellite access too.','Which dependencies remain during an emergency?'),
     ('Cultural and community fit','Service design and governance should reflect how people actually use connectivity.','Who gets to define successful access?')])

add('did','Decentralised Identity','Infrastructure','⬡',
    'Approaches to digital credentials in which people or organisations can present verifiable claims.',
    'A training provider is considering portable digital credentials for learner achievements.',[
    ('Can let someone present a verifiable digital credential.','does','Proof of a claim is a central purpose of credential systems.'),
    ('Needs trusted issuers and verification methods.','needs','Recipients must be able to check who issued a claim.',True),
    ('Lost keys or credentials can make access difficult.','limits','Recovery and usability are major implementation challenges.'),
    ('Learners may gain greater portability for qualifications.','affects','Credential holders experience the service directly.'),
    ('Requires standards and interoperable data formats.','needs','Different wallets and systems must understand one another.',True),
    ('Can support selective disclosure in some designs.','does','Some credential protocols disclose only what is necessary.'),
    ('A cryptographic proof does not guarantee a claim is true.','limits','Issuers can be mistaken or dishonest despite valid signatures.'),
    ('Employers may need new verification processes.','affects','Organisations accepting credentials must adapt.'),
    ('Needs an accessible storage and recovery experience.','needs','People need to retain and regain control of their credentials.',True),
    ('Can reduce repeated manual checks of some documents.','does','Digital verification can simplify workflows.'),
    ('Depends on privacy-conscious revocation mechanisms.','needs','Expired or revoked credentials must be handled appropriately.'),
    ('Some people may lack suitable devices or digital skills.','limits','Digital-only systems can widen access gaps.')],
    [('Governance of trust','Technical verification cannot replace decisions about whose authority is legitimate.','Who decides which issuers are recognised?'),
     ('Consent and tracking','Even valid credentials can be used to profile people across services.','Can presentation be linked across organisations?'),
     ('Non-digital alternatives','A portable wallet should not become the only way to prove eligibility.','How does someone participate without a smartphone?')])

contexts = [
 {'id':'education','label':'Education & learning','question':'What must learners and teaching staff understand or be able to do, and who might be left out?'},
 {'id':'business','label':'Workplace & business','question':'How would this change work, skills, accountability and cost in a real organisation?'},
 {'id':'community','label':'Community & public life','question':'Whose voice or local knowledge should shape deployment, access and consent?'},
 {'id':'environment','label':'Environment & place','question':'What energy, materials, infrastructure and ecological effects may be hidden by the headline?'}
]
for t in T:
    assert len(set(c['id'] for c in t['cards'])) == 12
    assert set(c['layer'] for c in t['cards']) == {'does','needs','limits','affects'}
    assert sum(c['critical'] for c in t['cards']) == 3
    assert all(c['layer']=='needs' for c in t['cards'] if c['critical'])
    assert sum(c['layer']=='does' for c in t['cards'])==3
    assert sum(c['layer']=='needs' for c in t['cards'])==4
    assert sum(c['layer']=='limits' for c in t['cards'])==3
    assert sum(c['layer']=='affects' for c in t['cards'])==2
payload = {'version':1,'contexts':contexts,'technologies':T}
(ROOT/'assets/content.json').write_text(json.dumps(payload,ensure_ascii=False,indent=2)+'\n',encoding='utf-8')
(ROOT/'assets/content.js').write_text('/* Auto-generated from assets/content.json; also usable from file:// */\nwindow.TECH_XRAY_CONTENT = '+json.dumps(payload,ensure_ascii=False,separators=(',',':'))+';\n',encoding='utf-8')
print(f'Wrote {len(T)} technologies, {sum(len(x["cards"]) for x in T)} evidence cards, {sum(len(x["blindspots"]) for x in T)} hidden dependencies')

from django.shortcuts import render

# ============ MA'LUMOTLAR: shu yerni o'zingizga moslab o'zgartiring ============
# Rasm kerak bo'lsa: "img": "assets/images/proj1.jpg" (static/assets/images/ ichiga qo'ying)

PROFILE = {
    'logo': 'NAME',
    'first_name': 'Firstname',
    'last_name': 'Lastname',
    'intro': 'Write two short sentences about what you do and what you build.',
    'role': 'UI/UX DESIGNER',
    'job': ['WEB', 'DEVELOPER'],
    'about': 'Write your short story here: who you are, what you study or build, and what you care about.',
    'quote': 'Add a personal line that sums up how you think and work.',
    'email': 'you@example.com',
    'location': 'City, Country',
    'resume': '#',
    'socials': [('GH', '#'), ('in', '#'), ('IG', '#'), ('Pin', '#')],
    'contact_text': 'Tell people what you are open to: internships, full-time work, freelance projects, or just a chat.',
}

MINI = [
    ('◐', 'AI / ML', 'Short line about this.'),
    ('✎', 'UI / UX', 'Short line about this.'),
    ('♞', 'Chess', 'Short line about this.'),
    ('</>', 'Engineering', 'Short line about this.'),
]
STATS = [('5+', 'Projects'), ('2+', 'Years coding'), ('5+', 'Technologies'), ('∞', 'Curiosity')]
LANGS = [('English', 'Fluent'), ('Uzbek', 'Native'), ('Russian', 'Fluent'), ('Turkish', 'Basic')]

SKILLS = [
    ('</>', 'Programming Languages', ['Python', 'C', 'JavaScript']),
    ('◍', 'Web Development', ['HTML', 'CSS', 'React', 'Node.js']),
    ('≣', 'Databases', ['MySQL', 'PostgreSQL', 'MongoDB']),
    ('☁', 'Cloud Platforms', ['Google Cloud', 'Firebase']),
    ('✦', 'UI/UX & Design', ['Figma', 'Webflow', 'Canva']),
    ('⑂', 'Version Control', ['Git', 'GitHub']),
]

PROJECTS = [
    {'title': 'Project One', 'text': 'What this project does and why it matters, in two sentences.', 'tags': ['Python', 'AI'], 'url': '#', 'bg': 'linear-gradient(135deg,#0e1a3d,#05070d)', 'img': ''},
    {'title': 'Project Two', 'text': 'What this project does and why it matters, in two sentences.', 'tags': ['Node.js', 'MongoDB'], 'url': '#', 'bg': 'linear-gradient(135deg,#0d2a2f,#05070d)', 'img': ''},
    {'title': 'Project Three', 'text': 'What this project does and why it matters, in two sentences.', 'tags': ['React', 'Chart.js'], 'url': '#', 'bg': 'linear-gradient(135deg,#251340,#05070d)', 'img': ''},
    {'title': 'Project Four', 'text': 'What this project does and why it matters, in two sentences.', 'tags': ['NLP', 'Python'], 'url': '#', 'bg': 'linear-gradient(135deg,#102a44,#05070d)', 'img': ''},
]

MILESTONES = [
    ('Hackathon', 'Short line about this achievement.'),
    ('Team Leadership', 'Short line about this achievement.'),
    ('Event Management', 'Short line about this achievement.'),
    ('Public Speaking', 'Short line about this achievement.'),
]

INTERESTS = [
    {'title': 'Films', 'text': 'Describe what you love about this passion.', 'bg': 'linear-gradient(135deg,#3b0f2e,#0a0710)', 'img': ''},
    {'title': 'Chess', 'text': 'Describe what you love about this passion.', 'bg': 'linear-gradient(135deg,#3a2a12,#0a0710)', 'img': ''},
    {'title': 'Poster Design', 'text': 'Describe what you love about this passion.', 'bg': 'linear-gradient(135deg,#4a0f3a,#0a0710)', 'img': ''},
    {'title': 'Books', 'text': 'Describe what you love about this passion.', 'bg': 'linear-gradient(135deg,#14243f,#0a0710)', 'img': ''},
    {'title': 'Art', 'text': 'Describe what you love about this passion.', 'bg': 'linear-gradient(135deg,#4a2a0a,#0a0710)', 'img': ''},
]
# ================================================================


def home(request):
    return render(request, 'index.html', {
        'p': PROFILE, 'mini': MINI, 'stats': STATS, 'langs': LANGS, 'skills': SKILLS,
        'projects': PROJECTS, 'milestones': MILESTONES, 'interests': INTERESTS,
    })

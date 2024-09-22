const skillsInput = document.getElementById('skills-input');
const skillsBox = document.getElementById('skills-box');
const skillWarning = document.getElementById('skill-warning');
let skills = [];

skillsInput.addEventListener('keypress', function(e) {
    if (e.key === 'Enter') {
        e.preventDefault();
        const skill = skillsInput.value.trim().toLowerCase();

        if (skill && !skills.includes(skill)) {
            skills.push(skill);
            updateSkillsBox();
            skillsInput.value = '';
        } else if (skills.includes(skill)) {
            skillWarning.textContent = 'Skill already exists!';
            skillWarning.style.display = 'block';
            setTimeout(() => {
                skillWarning.style.display = 'none';
            }, 3000);
        }
    }
});

function updateSkillsBox() {
    skillsBox.innerHTML = '';

    skills.forEach(skill => {
        const skillItem = document.createElement('div');
        skillItem.classList.add('skill-item');
        skillItem.innerHTML = `${skill} <span class="remove" data-skill="${skill}">x</span>`;
        skillsBox.appendChild(skillItem);
    });

    const removeButtons = document.querySelectorAll('.remove');
    removeButtons.forEach(button => {
        button.addEventListener('click', function() {
            const skillToRemove = button.getAttribute('data-skill');
            skills = skills.filter(s => s !== skillToRemove);
            updateSkillsBox();
        });
    });
}

// Resume File Upload Handling
const resumeInput = document.getElementById('resume');
const resumeError = document.getElementById('resume-error');
const removeResumeButton = document.getElementById('remove-resume');

resumeInput.addEventListener('change', function() {
    const file = resumeInput.files[0];

    if (file && file.type !== 'application/pdf') {
        resumeError.textContent = 'Please upload a valid PDF file!';
        resumeError.style.display = 'block';
        resumeInput.value = ''; // Clear input
        removeResumeButton.style.display = 'none';
    } else {
        resumeError.style.display = 'none';
        removeResumeButton.style.display = 'inline';
    }
});

removeResumeButton.addEventListener('click', function() {
    resumeInput.value = '';
    removeResumeButton.style.display = 'none';
});

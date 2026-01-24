# Still Asking

	


_Still Asking_ is a new experimental newsletter, born out of a desire to explore small doses of history and philosophy daily on the commute to work. Each essay dives into either a single thinker, from Plato to modern philosophers like Hanna Arendt, or a single historical event, like the Great Schism of 1054 or the start of WWI. I won't trod out particularly new events, with the aim to revisit seminal philosophers and moments in history.


> Americans no longer talk to each other, they entertain each other. They do not exchange ideas, they exchange images. They do not argue with propositions; they argue with good looks, celebrities and commercials. — **Neil Postman, Amusing Ourselves to Death**

_Still Asking_ is a new experimental newsletter, born out of a desire to explore small doses of history and philosophy daily on the commute to work. Each essay dives into either a single thinker, from Plato to modern philosophers like Hanna Arendt, or a single historical event, like the Great Schism of 1054 or the start of WWI. I won't trod out particularly new events, with the aim to revisit seminal philosophers and moments in history.

I have always found reading history to be an antidote to the fracturing of my attention that takes place slowly with scrolling social media or different news sites. Giving myself a few minutes to engage with a perhaps familiar but old idea is a little antidote I'm hoping to provide both for myself and for the reader.

Occasionally, mixed in with the purely historical and philosophical topics a more substantial piece will be written with modern reflections. These won’t necessarily be scheduled and may be entirely ad-hoc.

The daily articles will be written with a heavy dose of AI support, with human editing. This may be offensive to some which is understandable. The benefit of using AI in this case is that much of the information being presented is already well known and large language models tend to be very good at the goal described, presenting existing well understood writing with a new varnish.

## Posts

{% for theme in links %}
* [{{ theme.title }}]({{ theme.path }})
  {% for child in theme.children %}
    * [{{ child.title }}]({{ child.path }})
  {% endfor %}
{% endfor %}

## Planned Themes

### 2026

1. **The Social Contract:** How we justify being "ruled." 14 days from Hobbes’s "state of nature" to Rousseau’s "General Will" and Rawls’s "Veil of Ignorance."
2. **The Printing Press & The Truth:** How a piece of hardware broke the Catholic Church’s monopoly on "reality," leading to the Scientific Revolution along with modern reflections like Neil Postman.
3. **Phases of the Roman Empire**: Walk through the phases of the Roman Empire from an initial Republic, through Augustus, explaining the change to Christianity and eventual downfall.
4. **The Anatomy of Tyranny:** How republics turn into autocracies. Using Plato’s "Five Regimes," Machiavelli’s _The Prince_, Montesquieu’s warnings on the separation of powers, Hannah Arendt’s modern works, and Friedrich Hayek's theory on the tyranny of central planning.
5. **The Industrial Mind:** How factories changed the human soul. Analyzing the alienation of the worker through Marx, Smith, and the Luddite movement.
6. **The Greeks**: Philosophy, literature and history from ancient Greece. Covers Plato, Aristotle, Homer, discussion of religion and culture.
7. **The Individual vs. The Collective:** A clash of worldviews. 14 days comparing J.S. Mill’s _On Liberty_ with the collectivist theories of Marx and Hegel.
8. **The Spark of WWII**: The unlikely series of events, explored in detail that sparked WWII.
9. **The Darwinian Earthquake:** How evolution shattered philosophy. The 14-day fallout of 1859, touching on Nietzsche’s "God is Dead" and the rise of Pragmatism (William James).
10. **Post-War Despair (Existentialism):** How the horrors of WWII gave birth to Sartre, Camus, and the search for meaning in a world that seemed to have none.
11. **History of Psychology**: Early writings in psychology from ancient Greece, India.
12. **Nature vs. Nurture**: Modern debates across psychology and sociology.
13. **Just War Theory:** Can killing be moral? 14 days tracking the "rules of war" from St. Augustine and Aquinas to Michael Walzer’s modern interpretations.
14. **The Art of Strategy:** Eastern vs. Western military thought. Comparing Sun Tzu’s _Art of War_ (deception/efficiency) with the brutalist realism of Thucydides. Clausewitz, a deep dive into _On War_, exploring "Absolute War" vs. "Real War" and the relationship between the General and the Statesman.
15. **The Measurement Problem:** How physics broke philosophy. Exploring how Quantum Theory (Bohr vs. Einstein) forced us to rethink the nature of reality itself.
16. **Property & Liberty:** Who "owns" the earth? Tracking the debate from John Locke’s "labor theory" to Proudhon’s "Property is Theft" and Hayek’s _Road to Serfdom_.
17. **The Death of Certainty:** How we know what is "true." From the Scholastic logic of the Middle Ages to Karl Popper’s "Falsification" and Thomas Kuhn’s "Paradigm Shifts."

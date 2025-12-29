# Still Asking

> Americans no longer talk to each other, they entertain each other. They do not exchange ideas, they exchange images. They do not argue with propositions; they argue with good looks, celebrities and commercials. — **Neil Postman, Amusing Ourselves to Death**

_Still Asking_ is a new experimental newsletter, born out of a desire to explore small doses of history, philosophy daily on the commute to work. Instead of engaging with purely entertainment topics the goal is to engage with something a little more substantial. I have always found reading history and engaging with past events to always been an antidote to madness of the present media culture. When engaging with history and thinkers from the past there is just an ability to pause and reflect unlike the in many ways how media is presented today.

With that, we introduce the idea of _Still Asking,_ a daily newsletter for the curious, the skeptical, and the intellectually hungry. We provide bite-sized, 3-minute essays that bridge the gap between the greatest thinkers of the past and the complexities of the present.

Every day, we deliver:

- One Thinker: From the stoic logic of Marcus Aurelius to the radical politics of Hannah Arendt.
- One Event: A moment in time—a battle, a discovery, or a scandal—where ideas met reality.
- Today’s Relevance: Why this “old” news is the key to understanding your morning headlines.

History is best understood in arcs. That’s why we organize our daily posts into 14-day thematic journeys. For two weeks, we might dive deep into the _Philosophy of War_, exploring how we justify conflict. The next two weeks, we might shift to _The History of the Dinner Plate_, looking at how trade and taste built the modern economy.

Occasionally, mixed in with the purely historical and philosophical topics a more substantial piece will be written with modern reflections. These won’t necessarily be scheduled and may be entirely ad-hoc.

The daily articles will be written with a heavy dose of AI support, with human editing. This may be offensive to some which is understandable. The benefit of using AI in this case is that much of the information being presented is already well known and large language models tend to be very good at the goal described, presenting existing well understood writing with a new varnish.

## Posts

{% for theme in links %}
* [{{ theme.title }}]({{ theme.path }})
  {% for child in theme.children %}
    * [{{ child.title }}]({{ child.path }})
  {% endfor %}
{% endfor %}

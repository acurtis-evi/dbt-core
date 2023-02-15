# dbt Core: So much to say (February 2023)

We're back, and we have way more to say than time to write it down. Is it a good thing? Maybe?

Since last August, we:
- Released dbt Core v1.3 and v1.4 - with Python models among other goodness
- Something about Transform?
- ...

Let's cut to the chase

This update is going to be a touch shorter, as we have many fewer surprises to share. That's a good thing. We've been talking more in public about what we're building: on [the blog](https://www.getdbt.com/blog/), on [the other (cooler) blog](https://docs.getdbt.com/blog), at [Staging](https://www.getdbt.com/blog/staging-highlights-the-latest-from-dbt-labs/), and in [GitHub discussions](https://github.com/dbt-labs/dbt-core/discussions). And, while the meta conceit was good once ("welcome to my mind, it's an improvised play in four acts, how's that for stream[-of-consciousness] transformation"), I don't want to risk overdoing it.

Here's what you came for:

| Version | When          | Namesake<sup>a</sup>      | Stuff | Confidence<sup>b</sup>  |
| ------- | ------------- | -------------- | ----- | ------------ |
| 1.1 ✅   | April        | Gloria Casarez | Testing framework for dbt-core + adapters. Tools and processes for sustainable OSS maintenance. | 100% |
| 1.2 ✅   | July         | Henry George   | Built-in support for grants. Migrate cross-db macros into dbt-core / adapters. Improvements to metrics. | 100% |
| 1.3 🌀   | October      |                | Python models in dbt. More improvements to metrics. (Other things, too—but those are the main events.) | 95% |
| 1.4 ⚒️    | Jan 2023     |                | Behind-the-scenes improvements to technical interfaces. A real, documented Python API/library, with an improved CLI to wrap it. Further investments in structured logging. | 80% |
| 1.5+ 💡  | Next year<sup>c</sup> |                | Multi-project deployments: split up the monolith. The same DAG, more active: external orchestration. Python in dbt: next steps. Start imagining dbt Core v2. | 50% |

`updated_at: 2023-02-15`

<sup>a</sup>Always a [phamous Philadelphian](https://en.wikipedia.org/wiki/List_of_people_from_Philadelphia), true to our roots. If you have ideas or recommendations for future version namesakes, my DMs are open :)

<sup>b</sup>dbt Core is, increasingly, a standard-bearer and direction-setter. We need to tell you about the things we're thinking about, long in advance of actually building them, because it has real impacts for the plans of data teams and the roadmaps of other tools in the ecosystem. We also know that we don't know now everything we will know a year from now. As new things come up, as you tell us which ones are important to you, we reserve the right to pivot. So we'll keep sharing our future plans, on an ongoing basis, wrapped in a confidence interval.

<sup>c</sup>We're sticking with one minor version release per quarter, for the foreseeable. I haven't split those out here because, 6+ months into the future, we care more about the _what_ and the _why_ than the _when_. As we get closer, we'll be able to detail the more-specific functionality that might land in specific releases. Note too that these ideas, though we're already devoting meaningful time and effort to thinking through them, are not definite commitments.

# Commentary

Hopefully, you're already well aware of, and happily making use of, the capabilities that shipped in dbt Core v1.1 and v1.2 earlier this year. If you're not, the [upgrade guides](https://docs.getdbt.com/guides/migration/versions) are a good place to get up to speed.

## v1.3 (October): Coalesce

I got to see a very small number of you a few months ago at a London dbt meetup, where I presented May's edition of roadmap. I'm looking forward—we're all (!) looking forward—to seeing and talking with many more of you in October for [Coalesce](https://coalesce.getdbt.com/). For those who are able and comfortable to make the trip to New Orleans, London, or Sydney—and for all the many more who are planning on a "classic Coalesce" experience, from the comfort of your laptop—we're very excited to have you.

The big thing coming in dbt Core v1.3 is support for Python models. You already knew that. All the details are in [the beta docs](https://docs.getdbt.com/docs/building-a-dbt-project/building-models/python-models), so give 'em a read now if you haven't yet.

There are a couple of FAQs (Frequently Associated Qualms) that I want to address, here and now, in case you're thinking one of them:

**Will I need to know Python to start using dbt?** Not at all. At the same time, if you don't know it, and want to learn, that's great! The open source Python-for-data ecosystem is powerful, and often also overwhelming. We'll be creating resources to help light the way, plus highlighting guides, walkthroughs, and recommendations made by members of the community.

**Is now the time to start experimenting with advanced statistical processing, predictive analytics, …?** Maybe! Or maybe not. Developing a solid, foundational set of data models should always come first. Deeply understand your data. Use it to power reliable analytical reporting. Whether you're ready to take the next step now or later, dbt is here to make it possible.

**Does adding Python fundamentally change the nature of dbt Core?** Honestly, yes and no.

- **No:** For all the SQL you're already writing and running successfully, we think you should keep it that way. SQL remains the most expedient and accessible way to write most forms of data transformation. We are *not* going to stop investing in dbt's support for SQL—and in Jinja as its templating engine, for the foreseeable future. (dbt-core v1.3 also includes a long-awaited upgrade to Jinja3, which should help folks installing alongside other Jinja-powered tools.)
- **Yes:** Adding support for Python has clarified our thinking on multilingual dbt. It's helped us realize that the real value of dbt is not in Jinja-templated SQL. (Anyone can build that in a weekend; many have.) It's the framework, the environment-aware workflow, the DAG, the integrated testing and documentation—more things than I can name here. That's more language-agnostic than you might expect. At the same time, each language brings its strengths; there will be things you can do in Python that you cannot do in Jinja-SQL, and vice versa.

Note that, while Python is the main event, it's not the only new thing coming in v1.3. Every release includes a bunch of exciting community contributions, and this one's got [something long awaited](https://docs.getdbt.com/reference/resource-configs/docs#custom-node-colors?version=1.3). We're also making improvements to metrics to support the launch of the **dbt Semantic Layer**. That's been a *huge* initiative, long in the works, and a long time coming. It's not my place to offer spoilers. I recommend you check out [Drew's blog](https://www.getdbt.com/blog/dbt-semantic-layer/), if you haven't already, and [join us for the show](https://coalesce.getdbt.com/).

## v1.4 (January): For us, for you, for Core

After Coalesce, we'll be taking stock of all that we built this year, and all we're looking to build next year. We are dedicating the months of November through January to dbt Core's technical foundations. (Plus: taking some well-deserved vacation over the holidays.)

This work is comprised of two big initiatives:

1. **API + CLI:** Improving and documenting dbt-core's internal Python APIs. Creating a new and better-constructed CLI to wrap around it. To be clear, this CLI will support all the same commands, flags, and arguments as it does today.
2. **Event + logging interface.** Supporting type-safe, language-agnostic ways to ingest structured logs produced by dbt-core. This will enable other tools (ours and yours) to provide reliable observability around dbt runs, as well as more-digestible and realer-time metadata. Over a longer term, providing more information in log events where it's missing today.

This is work that largely happens behind the scenes. If we do it well, the average dbt user should not notice any immediate differences. So why are we doing it?

**If you use dbt Core's CLI,** this will make it easier to manage the growing number and complexity of command line options. To make sure all the right flags and options are supported on all the right commands; to add and update help text; and to automatically coordinate updated documentation that's been, to date, hand crafted by resident artisans.

**If you build tools that wrap around dbt-core,** the appeal of a stable and documented API to its internals should be obvious. This is a long initiative, and we won't get to all of it right away, but the right idea is there. (And apologies, in advance, for the undocumented internal methods we'll be breaking in the process.)

**If you use dbt Cloud,** Core's ability to provide stable and sensible interfaces is a big part of what enables differentiated capabilities in dbt Cloud in the future. It's not the coolest stuff in its own right, but a necessary precondition for that cool stuff to exist.

**If you use dbt at all,** you should care about this work, insofar as it will make it easier for us to build more features faster next year. We want more people to join us in building dbt Core, and a welcoming codebase to greet them.

## v1.5+ (Next year)

If you've been following our GitHub discussions, or the Analytics Engineering roundup, none of these topics should come as too much of a surprise. They're neither definite commitments, nor the full set of things we expect to do next year. There's a lot of linear improvement to existing functionality that's always on our minds, and in our issues. But I want to start with the pair of ideas that we've been talking about nonstop, for which we're already dreaming up some code:

1. **Multi-project deployments.** `ref` a final model from someone else's project, wherever they've put it, without the need to run it first. Split up monolithic projects of 5000 models into 10 projects of 500, grouped by team and domain. This is more than just "namespacing": to really solve for this, we also need to solve for versioning and contracts, and support a variety of deployment mechanisms. The discussion for this has been in [#5244](https://github.com/dbt-labs/dbt-core/discussions/5244); I'll have more to share over the next few months.

2. **External orchestration.** The same dbt DAG, playing a more active role. We've been developing this idea internally, and have arrived at a few strong opinions. This would not be a new node type, but an upgrade to the ones we already have: sources, models, and exposures. Sources that can trigger their own ingest. Exposures that can trigger downstream data consumers (syncs, sinks, etc). Models that can define and run transformations in dedicated execution environments, reading from and writing back to centralized data storage. For each of those external integrations, a simple request where possible, and a dedicated plugin where justified. If you're someone who followed along the original "external nodes" discussion ([#5073](https://github.com/dbt-labs/dbt-core/discussions/5073))—especially if you've got a tool you'd be excited to integrate into dbt's DAG—let's talk.

---

We also intend to keep pushing on existing capabilities in dbt Core. Again, a non-exhaustive list:

**Python models, only just beginning.** What's the right DataFrame API to standardize on? Should dbt have a role in managing packages, model training, artifacts? Eventually, a full "MLOps" workflow? v1.3 in October will be our first foray, not the final story. Cody just opened some GitHub discussions, starting with [#5742](https://github.com/dbt-labs/dbt-core/discussions/5742). See what we're thinking, and weigh in.

**Adapters, adapters, adapters.** We want to make it easier to build, test, and validate support for dbt on a new database, query engine, or runtime environment. We want to support more than one adapter for use in a single dbt-core invocation. We want to keep honing the performance of caching, cataloging, and incremental processing at scale, across data platforms. We want to offer more adapters in dbt Cloud.

**Imagining dbt Core v2.** Last December, when announcing the v1.0 release, I predicted (wildly guessed) that dbt v2.0 would take 2-4 years to reach us (2023-2025). Then I put some things on a slide, asking everyone to imagine:
- *dbt-SQL: The same capabilities. No Jinja.*<sup>1</sup>
- *The docs are always ready.*<sup>2</sup>
- *One dbt run across many databases and query engines.*<sup>3</sup>
- *Define your own tasks for the dbt DAG.*<sup>4</sup>

Most of that still feels about right. I don't see us ending next year with a v2.0 final release, but I do see us having a clear picture of what v2 will look like. In a sense, we've already started the work to get there, by combing our way through the rougher edges of v1.

I'm excited for the next few months. I hope you are too.

---

<sup>1</sup>Now, I wonder if the answer is: Jinja-SQL and Python are just two of many supported languages for dbt Core. Some languages will make it dead-easy to unit test, to transpile across different databases, to infer column-level lineage. Others make it possible to run introspective queries that dynamically template transformation logic. It's an exciting future to consider. The challenge is to be clear and opinionated about what each one brings to the table, and when each one shines.

<sup>2</sup>Real-time metadata; see above.

<sup>3</sup>External orchestration; see above.

<sup>4</sup>This one, I'm not so sure! The task before us is the same as it ever was: build the DAG, as fast as possible, just what's needed, when it's needed. Still, I keep  more advanced use cases that want to programmatically create, manipulate, and invoking the dbt DAG—and they may well be more plausible in a future where dbt-core has a documented, contracted set of internal APIs. That would be advanced-level stuff, guardrails not included. You probably don't need (or want) it, and if you do, you know it.

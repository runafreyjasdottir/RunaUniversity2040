# IT107: Web Technologies & Internet Architecture
## Bachelor of Science in Information Technology — University of Yggdrasil, 2040

**Credits:** 4
**Prerequisites:** IT101 (Foundations of Information Technology), IT105 (Programming for IT)
**Description:** A comprehensive study of the technologies, protocols, and architectures that constitute the World Wide Web and the broader Internet. Students examine the full stack of web development — from HTTP and TCP/IP through HTML, CSS, and JavaScript to server-side frameworks, databases, and deployment — and learn to build, secure, and troubleshoot modern web applications. By 2040, the web is not merely a platform for documents but the primary substrate for global software delivery, commerce, communication, and governance. Understanding its architecture is essential for any IT professional who builds, maintains, or secures information systems. The course includes extensive lab work: students build a complete web application from scratch, deploy it to the Yggdrasil Cloud, and defend it against simulated attacks.

---

## Lecture 1: The Web as Platform — Architecture, History, and Evolution

The World Wide Web was invented by Tim Berners-Lee at CERN in 1989 as a system for sharing scientific documents. Three decades later, it has become the primary platform for software delivery, commerce, communication, entertainment, and governance. This lecture examines the architectural principles of the web, its evolution through distinct eras, and the forces that have shaped its trajectory.

**The original web** (1989–1995) was a simple document system: HTML pages with hyperlinks, served by HTTP over TCP/IP, viewed by browser clients. The **early dynamic web** (1995–2005) introduced server-side scripting (CGI, PHP, ASP, JSP) that generated HTML from databases. The **AJAX era** (2005–2010) enabled asynchronous JavaScript requests, allowing pages to update without full reloads. The **single-page application (SPA) era** (2010–2020) moved much of the application logic to the browser, with frameworks like Angular, React, and Vue. The **serverless and edge era** (2020–2030) decomposed applications into functions and pushed computation closer to users. The **AI-augmented web** (2030–2040) integrates generative AI into every layer: AI-generated content, AI-personalised interfaces, AI-assisted development, and AI-driven security.

**The web architecture** is defined by several key principles. **Client-server model:** browsers (clients) request resources from web servers. **Statelessness:** HTTP is a stateless protocol; each request is independent, and server-side state is managed through cookies, sessions, or tokens. **Layered system:** proxies, caches, load balancers, and CDNs sit between client and server, transparently improving performance and reliability. **Uniform interface:** resources are identified by URIs, manipulated through standard methods (GET, POST, PUT, DELETE), and represented in standard formats (HTML, JSON, XML). **Cacheability:** responses explicitly declare whether they can be cached, enabling aggressive caching at multiple layers.

**The web in 2040** is both more powerful and more complex than its ancestors. **WebAssembly (Wasm)** enables near-native performance for compute-intensive tasks in the browser. **Progressive Web Apps (PWAs)** provide app-like experiences with offline capability, push notifications, and hardware access. **WebGPU** exposes GPU compute to web applications, enabling machine learning and scientific simulation in the browser. **WebTransport** (built on QUIC) provides low-latency, bidirectional communication for real-time applications. **Federated protocols** (ActivityPub, Matrix, Bluesky's AT Protocol) enable decentralised social networking, challenging the platform monopolies of the 2010s and 2020s. The **Semantic Web** (Berners-Lee's original vision, finally gaining traction in the 2030s) enables machines to understand the meaning of web content through structured data (JSON-LD, RDF), linked open data, and knowledge graphs.

**Required Reading:**
- Tim Berners-Lee, "Information Management: A Proposal" (CERN, 1989)
- Roy T. Fielding, "Architectural Styles and the Design of Network-based Software Architectures," PhD thesis, UC Irvine (2000)
- Ilya Grigorik, *High Performance Browser Networking* (O'Reilly, 2013/2035), ch. 1–3
- Alex Russell, "The Mobile Web: MIA" (2015/2035) and "The Mobile Web: Found" (2030)
- University of Yggdrasil, "The Yggdrasil Web Observatory: A Longitudinal Study of Web Architecture, 1995–2040" (2039)

**Discussion Questions:**
1. The web was designed for documents but evolved into an application platform. Is this evolution a natural extension of its architecture, or has it distorted the web into something it was never meant to be?
2. The Semantic Web was proclaimed in the early 2000s but only gained traction in the 2030s. Was the delay due to technical limitations, lack of incentive, or something else?
3. Federated protocols promise to decentralise social media, but most users remain on centralised platforms. Is federation a genuine alternative, or will network effects always favour centralisation?

---

## Lecture 2: HTTP and the Transport Layer — Protocols, Methods, and Status Codes

HTTP (Hypertext Transfer Protocol) is the application-layer protocol that powers the web. This lecture examines HTTP in depth: its methods, headers, status codes, versions, and the underlying transport protocols (TCP, TLS, QUIC) that carry it.

**HTTP methods** define the action to be performed on a resource. **GET** retrieves a resource; it is safe (does not modify state) and idempotent (repeating it has the same effect). **POST** submits data to be processed; it is neither safe nor idempotent. **PUT** replaces a resource entirely; it is idempotent. **PATCH** partially updates a resource; it is not necessarily idempotent. **DELETE** removes a resource; it is idempotent. **HEAD** retrieves headers without the body; **OPTIONS** retrieves supported methods; **TRACE** echoes the request (rarely used, often disabled for security). In 2040, **QUERY** (proposed in RFC 9536, 2038) provides a safe, idempotent method for complex queries that would be too long for GET.

**HTTP status codes** indicate the result of a request. **1xx (Informational):** 100 Continue, 101 Switching Protocols. **2xx (Success):** 200 OK, 201 Created, 204 No Content. **3xx (Redirection):** 301 Moved Permanently, 302 Found, 304 Not Modified. **4xx (Client Error):** 400 Bad Request, 401 Unauthorized, 403 Forbidden, 404 Not Found, 429 Too Many Requests. **5xx (Server Error):** 500 Internal Server Error, 502 Bad Gateway, 503 Service Unavailable, 504 Gateway Timeout. Understanding status codes is essential for debugging: a 502 often indicates a downstream server failure; a 429 suggests rate limiting; a 503 with a `Retry-After` header indicates temporary overload.

**HTTP headers** carry metadata. **Request headers:** `Host` (virtual host selection), `User-Agent` (client identification), `Accept` (content negotiation), `Authorization` (authentication), `Cookie` (state management), `If-None-Match` (conditional requests with ETags). **Response headers:** `Content-Type` (MIME type), `Content-Length` (body size), `Location` (redirection target), `Set-Cookie` (state management), `Cache-Control` (caching directives), `Strict-Transport-Security` (HSTS), `Content-Security-Policy` (CSP). In 2040, **new headers** have been introduced: `AI-Generated` (indicates AI-generated content, mandated by the EU Digital Transparency Act of 2033), `Privacy-Budget` (for differential privacy in analytics), and `Carbon-Footprint` (indicates the estimated carbon cost of serving the request, part of the Nordic Green Web initiative).

**HTTP versions** have evolved significantly. **HTTP/1.0** (1996) was simple but inefficient (one request per TCP connection). **HTTP/1.1** (1997) introduced persistent connections, pipelining, and chunked transfer. **HTTP/2** (2015) added multiplexing (multiple requests per connection), server push, and header compression (HPACK). **HTTP/3** (2022/2040), built on **QUIC** (a UDP-based transport with built-in TLS 1.3), eliminates head-of-line blocking and reduces connection latency. In 2040, HTTP/3 is the dominant protocol for web traffic, though HTTP/2 and HTTP/1.1 persist for legacy systems.

**Required Reading:**
- Roy T. Fielding & Julian F. Reschke, *HTTP Semantics* (RFC 9110, IETF, 2022/2035)
- Mark Nottingham, *HTTP Caching* (RFC 9111, IETF, 2022/2035)
- Jana Iyengar & Martin Thomson, *QUIC: A UDP-Based Multiplexed and Secure Transport* (RFC 9000, IETF, 2021)
- Lucas Pardue, *HTTP/3 and QUIC: The Future of the Web* (O'Reilly, 2030), ch. 1–3
- University of Yggdrasil, "The Bifröst Protocol: HTTP/3 Performance in the Nordic Region" (2039)

**Discussion Questions:**
1. HTTP methods are sometimes used incorrectly (e.g., GET for actions that modify state). Is this misuse a genuine problem, or is HTTP's simplicity a virtue that should not be complicated by strict method semantics?
2. HTTP/3's adoption required significant infrastructure changes (QUIC support in load balancers, firewalls, and CDNs). Was the performance gain worth the transition cost, or should the industry have stayed with HTTP/2?
3. The `AI-Generated` header mandates transparency about AI-generated content. Does this header actually help users make informed decisions, or is it merely a compliance checkbox that content creators circumvent?

---

## Lecture 3: HTML and the Document Object Model — Structure, Semantics, and Accessibility

HTML (Hypertext Markup Language) is the structural language of the web. This lecture covers HTML5 and its 2040 extensions, the Document Object Model (DOM), and the principles of accessible web design.

**HTML5** (standardised in 2014, with ongoing evolution through the WHATWG Living Standard) introduced semantic elements: `<header>`, `<nav>`, `<main>`, `<article>`, `<section>`, `<aside>`, `<footer>`, `<figure>`, `<figcaption>`, `<time>`, `<mark>`, and `<details>`. These elements give meaning to document structure, improving accessibility, SEO, and machine readability. **Forms** in HTML5 include new input types (`email`, `url`, `tel`, `date`, `range`, `color`) and validation attributes (`required`, `pattern`, `min`, `max`). **Multimedia** is native: `<video>` and `<audio>` elements with `<track>` for subtitles. **Canvas** and **SVG** provide raster and vector graphics. **Web Storage** (`localStorage`, `sessionStorage`) and **IndexedDB** provide client-side data persistence.

**The DOM (Document Object Model)** is the tree-structured representation of an HTML document in memory. Each HTML element is a **node** in the tree, with properties (attributes, text content, styles) and methods (insertion, deletion, traversal). JavaScript manipulates the DOM to create dynamic user interfaces. **DOM traversal** uses properties like `parentNode`, `childNodes`, `firstChild`, `lastChild`, `nextSibling`, `previousSibling`. **DOM manipulation** uses methods like `createElement`, `appendChild`, `removeChild`, `insertBefore`, `setAttribute`, `getElementById`, `querySelector`, `querySelectorAll`. In 2040, the **Shadow DOM** (part of Web Components) enables encapsulation: a component's internal DOM is hidden from the outer document, preventing CSS and JavaScript conflicts.

**Accessibility (a11y)** is the practice of making web content usable by people with disabilities. The **Web Content Accessibility Guidelines (WCAG 3.0, 2030)** define four principles: **Perceivable** (information must be presentable in ways users can perceive); **Operable** (interface components must be operable by all users); **Understandable** (information and operation must be understandable); and **Robust** (content must work with current and future assistive technologies). Practical techniques include: semantic HTML (using `<button>` instead of `<div onclick>`), **ARIA attributes** (`role`, `aria-label`, `aria-describedby`, `aria-live`), keyboard navigation (focus management, skip links), colour contrast (minimum 4.5:1 for normal text), and screen reader testing (NVDA, JAWS, VoiceOver). In 2040, **AI-powered accessibility tools** automatically generate alt text for images, transcribe audio, and suggest accessibility improvements during development.

**Lab Exercise:** Students build a static HTML page for a fictional University department. The page must: use semantic HTML5 elements; include a form with validation; embed a video with captions; use ARIA attributes for screen reader compatibility; and pass automated accessibility checks (WAVE, axe-core) with zero errors.

**Required Reading:**
- Ian Hickson et al., *HTML Living Standard* (WHATWG, 2040)
- Eric Freeman & Elisabeth Robson, *Head First HTML and CSS* (2nd ed., O'Reilly, 2012/2035), ch. 1–8
- Léonie Watson, *Introduction to Web Accessibility* (A Book Apart, 2035)
- W3C, *Web Content Accessibility Guidelines (WCAG) 3.0* (2030)
- University of Yggdrasil, "Accessibility at Yggdrasil: Policy, Practice, and Automated Compliance" (2039)

**Discussion Questions:**
1. Semantic HTML improves accessibility and SEO, but many developers still use `<div>` and `<span>` for everything, adding ARIA attributes to compensate. Is ARIA a legitimate fallback, or does its overuse indicate a failure to learn basic HTML?
2. The DOM is a tree, but modern web applications often treat it as a mutable database. Has the abstraction of virtual DOM (React, Vue) made developers less aware of the actual DOM structure and its performance implications?
3. AI-generated alt text is now standard, but it sometimes misdescribes images or misses cultural context. Should alt text always be human-written, or is AI-generated text sufficient for most cases?

---

## Lecture 4: CSS — Layout, Design, and Responsive Architecture

CSS (Cascading Style Sheets) is the presentation language of the web. This lecture covers CSS fundamentals, modern layout systems (Flexbox, Grid), responsive design, and the CSS architecture patterns of 2040.

**CSS fundamentals** include: **selectors** (element, class, ID, attribute, pseudo-class, pseudo-element, combinators); **the cascade** (source order, specificity, inheritance); **the box model** (content, padding, border, margin); **units** (px, em, rem, %, vw, vh, ch, fr); **colours** (hex, rgb, hsl, oklch, named colours); and **typography** (font-family, font-size, font-weight, line-height, letter-spacing). **CSS variables** (custom properties, `--primary-color: #0066cc`) enable theming and reuse. **CSS functions** (`calc()`, `clamp()`, `min()`, `max()`) enable dynamic calculations. **CSS animations** (`@keyframes`, `transition`, `animation`) bring motion to interfaces.

**Flexbox** (Flexible Box Layout, 2009/2015) is a one-dimensional layout system for arranging items in a row or column. It solves the classic problems of vertical centreing, equal-height columns, and dynamic spacing. Key properties: `display: flex` on the container; `flex-direction` (row/column); `justify-content` (main-axis alignment); `align-items` (cross-axis alignment); `flex-wrap` (wrapping); and `flex` (grow, shrink, basis) on items. Flexbox is ideal for: navigation bars, card layouts, form alignments, and any component-level layout.

**CSS Grid** (2017/2040) is a two-dimensional layout system for arranging items in rows and columns simultaneously. It is the most powerful layout tool in CSS history. Key properties: `display: grid` on the container; `grid-template-columns` and `grid-template-rows` (defining tracks with `repeat()`, `minmax()`, and `fr` units); `grid-gap` (spacing between tracks); `grid-column` and `grid-row` (placing items); and `grid-area` (named grid areas). Grid is ideal for: page-level layouts (header, sidebar, main, footer), complex dashboards, and magazine-style designs. In 2040, **subgrid** (nested grids that inherit track definitions from the parent) enables component-level grid alignment.

**Responsive design** ensures that web pages work well on all devices (desktops, tablets, phones, watches, TVs). **Media queries** (`@media (min-width: 768px) { ... }`) apply different styles at different viewport sizes. **Mobile-first design** starts with the smallest viewport and adds complexity for larger screens. **Fluid layouts** use percentages and `fr` units rather than fixed widths. **Responsive images** (`srcset`, `sizes`, `<picture>`) serve appropriately sized images. **Container queries** (`@container (min-width: 400px) { ... }`), standardised in 2023, allow components to respond to their container's size rather than the viewport — a major advance in component-driven design.

**CSS architecture** in 2040 emphasises maintainability at scale. **BEM** (Block Element Modifier) is a naming convention that prevents specificity wars. **Utility-first CSS** (Tailwind CSS) provides atomic utility classes that are composed in HTML, reducing CSS file size and eliminating unused styles. **CSS-in-JS** (styled-components, Emotion) embeds styles in JavaScript components, enabling dynamic theming and scoped styles. **Design tokens** (variables for colours, spacing, typography, breakpoints) are stored as JSON and transformed into CSS, iOS, Android, and Flutter styles, ensuring consistency across platforms. The **Yggdrasil Design System** — used for all University web properties — is built on design tokens, Tailwind CSS, and CSS custom properties.

**Required Reading:**
- Eric A. Meyer & Estelle Weyl, *CSS: The Definitive Guide* (5th ed., O'Reilly, 2023/2035), ch. 1–6, 12–14
- Rachel Andrew, *The New CSS Layout* (A Book Apart, 2017/2035), ch. 3–5 (Flexbox and Grid)
- Adam Wathan, *Tailwind CSS* (documentation, 2040)
- Una Kravets, "Container Queries: A Responsive Revolution" (CSS-Tricks, 2023/2035)
- University of Yggdrasil, "The Yggdrasil Design System: Tokens, Tailwind, and Cross-Platform Consistency" (2039)

**Discussion Questions:**
1. CSS has a reputation for being difficult to learn and frustrating to debug. Is this reputation deserved, or does it reflect a misunderstanding of the cascade and specificity?
2. Utility-first CSS (Tailwind) is polarising: proponents praise its productivity and consistency; critics decry its HTML verbosity and loss of semantic meaning. Is utility-first CSS a genuine advance or a regression to inline styles?
3. Container queries enable component-level responsiveness, but they add complexity to the CSS engine. Do container queries solve more problems than they create, or do they merely shift complexity from JavaScript to CSS?

---

## Lecture 5: JavaScript — The Language of the Browser

JavaScript is the programming language of the web. This lecture covers the core language, the browser environment, and the modern JavaScript ecosystem of 2040.

**JavaScript fundamentals** include: **types** (number, string, boolean, null, undefined, symbol, bigint, object, array, function); **variables** (`var`, `let`, `const` — `const` is preferred for immutability); **operators** (arithmetic, comparison, logical, bitwise, ternary, nullish coalescing `??`, optional chaining `?.`); **control flow** (`if/else`, `switch`, `for`, `while`, `do/while`, `for...of`, `for...in`); **functions** (declarations, expressions, arrow functions, IIFEs, generators, async functions); and **objects** (literal notation, constructors, classes, prototypes, destructuring). **TypeScript** (a statically typed superset of JavaScript) is the standard for large applications in 2040; it compiles to JavaScript and provides type checking, interfaces, generics, and advanced IDE support.

**The browser environment** includes: **the DOM API** (`document.getElementById`, `element.addEventListener`, `document.createElement`); **the BOM (Browser Object Model)** (`window`, `navigator`, `location`, `history`, `screen`); **timers** (`setTimeout`, `setInterval`, `requestAnimationFrame`); **storage** (`localStorage`, `sessionStorage`, `IndexedDB`); **networking** (`XMLHttpRequest`, `fetch`, `WebSocket`, `EventSource`); and **multimedia** (`AudioContext`, `CanvasRenderingContext2D`, `WebGL`, `WebGPU`). **Events** are the backbone of interactivity: click, submit, input, change, keydown, mousemove, scroll, resize, load, DOMContentLoaded. **Event delegation** (attaching a single listener to a parent element rather than many listeners to child elements) improves performance and simplifies dynamic content.

**Asynchronous JavaScript** is essential for non-blocking I/O. **Callbacks** were the original pattern but led to "callback hell." **Promises** (`then`, `catch`, `finally`, `Promise.all`, `Promise.race`) improved readability. **Async/await** (ES2017) provides syntactic sugar over Promises, making asynchronous code look synchronous: `const data = await fetch('/api/users').then(r => r.json())`. In 2040, **top-level await** is standard in modules, and **Promise.withResolvers** (ES2024) provides a cleaner way to create deferred Promises. **Web Workers** enable multithreading: scripts run in background threads, communicating with the main thread via message passing. **Service Workers** intercept network requests, enabling offline access, background sync, and push notifications.

**The JavaScript ecosystem** in 2040 includes: **bundlers** (Vite, esbuild, Rollup, webpack) that transform and optimise source code for production; **transpilers** (TypeScript, Babel, SWC) that convert modern syntax to compatible code; **linters** (ESLint, oxlint) that enforce code quality; **formatters** (Prettier, dprint) that enforce style; **testing frameworks** (Vitest, Jest, Playwright, Cypress) for unit and end-to-end testing; and **package managers** (npm, yarn, pnpm, bun) that manage dependencies. The **ecosystem churn** — the rapid obsolescence of tools and frameworks — is a perennial criticism of JavaScript development. In 2040, the industry has partially stabilised around **Vite** (build tool), **Vitest** (test runner), **TypeScript** (type system), and **React/Vue/Svelte** (UI frameworks), but innovation continues.

**Required Reading:**
- Marijn Haverbeke, *Eloquent JavaScript* (4th ed., No Starch Press, 2024/2035), ch. 1–6, 11, 13
- Axel Rauschmayer, *JavaScript for Impatient Programmers* (2nd ed., 2022/2035), ch. 1–4
- Anders Hejlsberg, "The Design of TypeScript" (Microsoft, 2035 white paper)
- Addy Osmani, *Learning JavaScript Design Patterns* (2nd ed., O'Reilly, 2012/2035), ch. 1–5
- University of Yggdrasil, "Modern JavaScript at Yggdrasil: Vite, TypeScript, and the Standard Frontend Stack" (2039)

**Discussion Questions:**
1. JavaScript was designed in 10 days and has accumulated numerous design flaws (implicit coercion, `this` binding, `var` hoisting). Is the language's success despite its flaws a testament to the web platform, or would a cleaner language (e.g., Dart, ReasonML) have been better?
2. TypeScript adds static types to JavaScript but compiles away at runtime. Is TypeScript a genuine improvement in reliability, or does it merely shift errors from runtime to compile time without reducing the total number of errors?
3. The JavaScript ecosystem is notorious for churn: frameworks rise and fall, build tools are replaced annually, and "best practices" change constantly. Is this churn a sign of healthy innovation or of an immature discipline?

---

## Lecture 6: Server-Side Development — Node.js, Python, and the Backend Stack

Web applications require server-side code to handle business logic, database access, authentication, and API endpoints. This lecture covers the server-side technologies and architectural patterns that power modern backends.

**Node.js** (Ryan Dahl, 2009) brought JavaScript to the server. Its **event-driven, non-blocking I/O model** enables high concurrency on a single thread, making it ideal for I/O-bound applications (APIs, real-time chat, streaming). **Express.js** (and its 2040 successors: **Fastify**, **NestJS**, **Hono**) provide web frameworks for routing, middleware, and request handling. **npm** (Node Package Manager) is the largest package ecosystem in the world, though it is also criticised for dependency bloat and supply chain vulnerabilities. In 2040, **Deno** (Dahl's successor to Node.js, with built-in TypeScript, security sandboxing, and standard library) and **Bun** (a fast JavaScript runtime written in Zig) are viable alternatives, but Node.js remains dominant.

**Python** is a popular backend language, especially for data-driven applications. **Django** is the "batteries-included" framework: it provides ORM, authentication, admin interface, form handling, and security features out of the box. **Flask** is the minimal framework: it provides routing and request handling, with everything else as extensions. **FastAPI** (introduced in 2018, dominant by 2030) is the modern choice: it uses Python type hints for automatic API documentation (OpenAPI/Swagger), validation (Pydantic), and serialisation. **ASGI** (Asynchronous Server Gateway Interface) servers (Uvicorn, Hypercorn) run async Python frameworks. In 2040, **FastAPI + Uvicorn + PostgreSQL + Redis** is a standard Python backend stack.

**API design** is a critical skill. **REST** (Representational State Transfer) uses standard HTTP methods and status codes, with resources identified by URIs. **GraphQL** (Facebook, 2015) allows clients to request exactly the data they need, reducing over-fetching and under-fetching. **gRPC** (Google, 2016) uses Protocol Buffers for efficient binary serialisation and HTTP/2 for transport, ideal for microservices. **WebSocket** provides full-duplex, persistent connections for real-time applications. In 2040, **tRPC** provides end-to-end type safety for TypeScript APIs, and **Server-Sent Events (SSE)** is the preferred alternative to WebSocket for server-to-client streaming.

**Authentication and authorisation** secure backend APIs. **Session-based auth** stores session IDs in cookies; it is simple but does not scale well across multiple servers. **Token-based auth** (JWT — JSON Web Tokens) stores authentication state in signed tokens; it scales well but requires careful handling of token revocation. **OAuth 2.0 / OpenID Connect** delegates authentication to identity providers (Google, Microsoft, the University's *Yggdrasil Identity Service*). **API keys** are used for service-to-service authentication. **Mutual TLS (mTLS)** provides certificate-based authentication for microservices. In 2040, **WebAuthn / FIDO2** provides passwordless authentication using hardware security keys or biometrics.

**Required Reading:**
- Ryan Dahl, "Node.js Design Patterns" (Packt, 2020/2035), ch. 1–4
- Sebastián Ramírez, "FastAPI Documentation" (2040)
- Roy T. Fielding, "REST APIs Must Be Hypertext-Driven" (2008/2035)
- Ilya Grigorik, "High Performance Browser Networking," ch. 15 ("WebSocket")
- University of Yggdrasil, "The Yggdrasil API Gateway: Routing, Authentication, and Rate Limiting for 500+ Microservices" (2039)

**Discussion Questions:**
1. Node.js enables high concurrency but is single-threaded; CPU-bound tasks block the event loop. Is Node.js genuinely suitable for general-purpose backends, or should it be restricted to I/O-bound applications?
2. GraphQL solves over-fetching but introduces new problems (complexity analysis, caching difficulties, N+1 queries). Is GraphQL a net improvement over REST, or does it merely trade one set of problems for another?
3. Passwordless authentication (WebAuthn/FIDO2) is more secure than passwords, but it requires hardware tokens or biometric sensors. Is passwordless authentication accessible to all users, or does it exclude those who cannot afford hardware tokens or who have disabilities that prevent biometric use?

---

## Lecture 7: Databases for the Web — SQL, NoSQL, and the Data Layer

Web applications require persistent storage. This lecture covers the database technologies and data access patterns used in web development, from traditional relational databases to modern distributed systems.

**Relational databases** remain the default choice for web applications. **PostgreSQL** is the leading open-source option: it supports advanced features (JSONB, full-text search, GIS, window functions, common table expressions), and it is the database of choice for the Yggdrasil web stack. **MySQL / MariaDB** is widely used in shared hosting and legacy applications. **SQLite** is used for development, testing, and embedded applications. **ORMs** (Object-Relational Mappers) bridge the gap between object-oriented code and relational tables: **SQLAlchemy** (Python), **Prisma** (TypeScript/Node.js), **ActiveRecord** (Ruby), **Eloquent** (PHP), **Hibernate** (Java). ORMs improve productivity but can generate inefficient queries; **query optimisation** (understanding `EXPLAIN ANALYZE`, indexes, query plans) remains an essential skill.

**NoSQL databases** serve specific use cases. **Document stores** (MongoDB, Couchbase, Firestore) store JSON-like documents, ideal for flexible schemas and rapid prototyping. **Key-value stores** (Redis, DynamoDB, etcd) provide fast, simple lookups, often used for caching, sessions, and configuration. **Wide-column stores** (Cassandra, ScyllaDB) handle massive write throughput and time-series data. **Graph databases** (Neo4j, Amazon Neptune) model relationships, used for social networks, recommendation engines, and fraud detection. **Search engines** (Elasticsearch, OpenSearch, Meilisearch, Typesense) provide full-text search, faceting, and relevance ranking. In 2040, **multi-model databases** (ArangoDB, OrientDB, Cosmos DB) support multiple data models (document, graph, key-value) in a single system, reducing the need for polyglot persistence.

**Caching** improves performance by storing frequently accessed data in fast memory. **Application-level caching** (Redis, Memcached) stores query results, rendered pages, and session data. **CDN caching** (Cloudflare, Fastly, Akamai) stores static assets (images, CSS, JavaScript) at edge locations close to users. **Database query caching** stores the results of expensive queries. **HTTP caching** (Cache-Control, ETag, Last-Modified) allows browsers and proxies to cache responses. **Cache invalidation** is one of the hard problems in computer science: when data changes, all cached copies must be updated or evicted. **Cache warming** pre-populates the cache before peak traffic. In 2040, **AI-driven cache prediction** anticipates which data will be needed and pre-fetches it, improving cache hit rates by 20–40%.

**Data consistency** in distributed web applications requires careful design. **ACID** (Atomicity, Consistency, Isolation, Durability) transactions ensure data integrity in relational databases. **BASE** (Basically Available, Soft state, Eventual consistency) describes the relaxed guarantees of NoSQL systems. **Sagas** and **event sourcing** manage transactions across microservices. **CQRS** (Command Query Responsibility Segregation) separates read and write models, optimising each independently. In 2040, **distributed SQL databases** (CockroachDB, Google Spanner, YugabyteDB) provide ACID transactions across geographically distributed nodes, but with latency trade-offs.

**Required Reading:**
- Hector Garcia-Molina, Jeffrey D. Ullman & Jennifer Widom, *Database Systems: The Complete Book* (2nd ed., 2009/2035), ch. 6–7
- Martin Kleppmann, *Designing Data-Intensive Applications* (O'Reilly, 2017/2035), ch. 1–2, 5–7
- Luc Perkins et al., *Seven Databases in Seven Weeks* (2nd ed., Pragmatic Bookshelf, 2018/2035), ch. 1 (PostgreSQL), ch. 4 (Redis), ch. 6 (Elasticsearch)
- Redis Documentation, "Caching Patterns and Strategies" (2040)
- University of Yggdrasil, "MímirDB: The University's Distributed Database for Web Applications" (2039)

**Discussion Questions:**
1. ORMs improve developer productivity but are often criticised for generating inefficient queries. Is the productivity gain worth the performance cost, or should developers write raw SQL for performance-critical paths?
2. Redis is frequently used as a cache, but it is also a database. Using Redis as a primary database (rather than a cache) is sometimes called "cache-as-database." Is this pattern legitimate, or does it risk data loss if the cache is evicted?
3. Distributed SQL databases promise ACID transactions at global scale, but they require consensus protocols that add latency. For a web application with users in Europe and Asia, is the consistency guarantee worth the ~100ms latency penalty?

---

## Lecture 8: Web Security — The OWASP Top Ten and Beyond

Web applications are the most common target for attackers. This lecture covers the major web security vulnerabilities, defensive coding practices, and the security architecture of modern web applications.

**Injection attacks** occur when untrusted data is sent to an interpreter as part of a command or query. **SQL injection** is the most dangerous: `SELECT * FROM users WHERE username = '$username'` becomes catastrophic if `$username` is `' OR '1'='1`. Defences: **parameterised queries** (prepared statements), **ORMs** (which use parameterised queries internally), and **input validation** (whitelist, not blacklist). **Command injection** (injecting shell commands through input fields), **LDAP injection**, and **XML injection** follow similar patterns. **NoSQL injection** (injecting into MongoDB queries) is less common but equally dangerous. In 2040, **static analysis tools** (SonarQube, Semgrep, CodeQL) automatically detect injection vulnerabilities in CI/CD pipelines.

**Cross-site scripting (XSS)** injects malicious scripts into web pages viewed by other users. **Reflected XSS** (malicious script in a URL parameter, reflected in the response) requires social engineering. **Stored XSS** (malicious script stored in the database, served to all users) is more dangerous. **DOM-based XSS** (malicious script manipulated by client-side JavaScript) is harder to detect. Defences: **output encoding** (HTML entity encoding, JavaScript encoding, URL encoding), **Content Security Policy (CSP)** (whitelisting allowed script sources), **HttpOnly cookies** (preventing JavaScript from accessing session cookies), and **trusted types** (enforcing safe DOM manipulation). In 2040, **AI-assisted XSS detection** (analysing JavaScript for dangerous patterns) is standard in security scanners.

**Authentication and session management** vulnerabilities include: weak passwords (mitigated by password policies, MFA, and passwordless auth); session fixation (attacker forces a known session ID on a victim); insecure session storage (session IDs in URLs or unencrypted cookies); and insufficient session expiration. **Broken authentication** (OWASP #2) remains a top vulnerability in 2040, often due to misconfigured identity providers or custom auth implementations. The defence: use standard, well-tested libraries (OAuth 2.0, OpenID Connect, WebAuthn) rather than rolling your own authentication.

**Other critical vulnerabilities** include: **Broken Access Control** (users can access resources they should not — e.g., by modifying URLs like `/user/123` to `/user/124`); **Cryptographic Failures** (using weak algorithms, hardcoded keys, or improper key management); **Insecure Design** (fundamental architectural flaws that cannot be fixed by coding practices alone); **Security Misconfiguration** (default passwords, unnecessary features, verbose error messages, unpatched systems); **Vulnerable and Outdated Components** (using libraries with known CVEs); **Identification and Authentication Failures** (weak MFA, brute-forceable login); **Software and Data Integrity Failures** (unverified updates, deserialization attacks); **Security Logging and Monitoring Failures** (insufficient logging enables attackers to operate undetected); and **Server-Side Request Forgery (SSRF)** (server makes requests to unintended internal resources). The **OWASP Top Ten 2035** (updated every 3–4 years) reflects these categories, with AI-specific attacks (prompt injection, model poisoning) added as a new category.

**Lab Exercise:** Students perform a **penetration test** on a deliberately vulnerable web application (the University's *Loki* training platform). They must: find and exploit an SQL injection vulnerability; escalate a reflected XSS to stored XSS; bypass broken access control to access another user's data; and write a remediation report for each finding.

**Required Reading:**
- OWASP, *OWASP Top Ten 2035* (<https://owasp.org/>, 2035)
- Dafydd Stuttard & Marcus Pinto, *The Web Application Hacker's Handbook* (2nd ed., Wiley, 2011/2035), ch. 1–5, 9–10
- Jim Manico & August Detlefsen, *Iron-Clad Java: Building Secure Web Applications* (Oracle Press, 2014/2035), ch. 1–3
- Troy Hunt, "Have I Been Pwned: The State of Data Breaches in 2040" (Pluralsight, 2040)
- University of Yggdrasil, "The Loki Platform: A Vulnerable Web Application for Security Training" (2039)

**Discussion Questions:**
1. SQL injection has been well understood for 25 years, yet it remains a top vulnerability. Is this due to developer ignorance, framework limitations, or the inherent difficulty of secure coding?
2. AI-assisted security scanning detects many vulnerabilities automatically, but it also generates false positives. Do the benefits of automated scanning outweigh the cost of triaging false positives?
3. The OWASP Top Ten focuses on technical vulnerabilities, but many breaches are caused by social engineering or insider threats. Should the Top Ten include human factors, or is that outside its scope?

---

## Lecture 9: Deployment, DevOps, and Site Reliability Engineering

Building a web application is only half the battle; deploying and operating it at scale is equally challenging. This lecture covers deployment strategies, CI/CD pipelines, containerisation, orchestration, and the principles of Site Reliability Engineering (SRE).

**Deployment strategies** balance risk and velocity. **Big-bang deployment** replaces the entire application at once; it is simple but risky. **Rolling deployment** replaces instances gradually (e.g., one server at a time), reducing risk but prolonging the deployment window. **Blue-green deployment** maintains two identical environments, switching traffic from the old (blue) to the new (green) instantly; it enables instant rollback but doubles infrastructure costs. **Canary deployment** routes a small percentage of traffic to the new version, monitoring for errors before increasing the percentage; it is the preferred strategy for high-risk changes. **A/B testing** routes traffic based on user segments, enabling experimentation with new features. In 2040, **AI-driven canary analysis** automatically detects anomalies in metrics (error rates, latency, throughput) and rolls back deployments that degrade performance.

**CI/CD pipelines** automate the build, test, and deployment process. **Continuous Integration (CI)** merges code changes frequently, running automated tests on each merge. **Continuous Delivery (CD)** automatically deploys code to staging or production after passing tests. **Pipeline stages** typically include: source control (Git); build (compiling, bundling); test (unit, integration, security, performance); artefact creation (Docker images, packages); deployment (to staging, then production); and verification (smoke tests, synthetic monitoring). **GitHub Actions**, **GitLab CI**, **Jenkins**, **CircleCI**, and **Azure DevOps** are the dominant CI/CD platforms in 2040. The University's *Völundr Pipeline* is a GitLab-based system that builds, tests, and deploys all University web applications.

**Containerisation and orchestration** package applications with their dependencies into portable units. **Docker** creates container images; **container registries** (Docker Hub, GitHub Container Registry, Amazon ECR) store them. **Kubernetes** orchestrates containers across clusters: deploying, scaling, load balancing, self-healing, and rolling updates. **Helm** packages Kubernetes applications. **Istio** provides service mesh capabilities (traffic management, security, observability). In 2040, **GitOps** (using Git as the single source of truth for infrastructure and application state) is the dominant deployment pattern: changes to Git automatically trigger reconciliation by tools like **ArgoCD** or **Flux**.

**Site Reliability Engineering (SRE)** is Google's approach to operations: applying software engineering principles to infrastructure and operations. **SRE principles** include: **error budgets** (allowing a certain rate of failures to balance reliability with velocity); **service level objectives (SLOs)** (quantitative reliability targets, e.g., 99.9% availability); **service level indicators (SLIs)** (metrics that measure SLOs, e.g., request latency, error rate); **blameless postmortems** (analysing incidents without assigning blame, focusing on systemic improvements); **toil reduction** (automating repetitive operational tasks); and **observability** (monitoring, logging, tracing, and alerting). In 2040, **AIOps** (AI for IT Operations) uses machine learning to detect anomalies, correlate alerts, predict failures, and suggest remediation — augmenting but not replacing human SREs.

**Required Reading:**
- Betsy Beyer et al., *Site Reliability Engineering: How Google Runs Production Systems* (O'Reilly, 2016/2035), ch. 1–3, 6, 8
- Gene Kim et al., *The DevOps Handbook* (2nd ed., IT Revolution, 2021/2035), ch. 2–5
- Niall Richard Murphy et al., *The Site Reliability Workbook* (O'Reilly, 2018/2035), ch. 1–2
- James Turnbull, *The Art of Monitoring* (James Turnbull, 2016/2035), ch. 1–4
- University of Yggdrasil, "The Völundr Pipeline: CI/CD for 200+ University Services" (2039)

**Discussion Questions:**
1. Canary deployment is the safest strategy but requires sophisticated monitoring and rollback mechanisms. For small teams with limited operational expertise, is canary deployment practical, or should they use simpler strategies (blue-green or rolling)?
2. GitOps promises to eliminate configuration drift by making Git the single source of truth, but it also creates a new attack surface (compromising Git can compromise production). Is GitOps genuinely more secure than traditional deployment methods?
3. AIOps detects anomalies automatically, but it can also generate alert fatigue if thresholds are poorly tuned. Is AIOps a net improvement over traditional monitoring, or does it merely automate the problem of too many alerts?

---

## Lecture 10: Performance Optimisation — Speed, Efficiency, and the User Experience

Web performance is not merely a technical concern; it directly impacts user engagement, conversion rates, and search rankings. This lecture covers the techniques and tools for measuring and improving web performance.

**Performance metrics** quantify the user experience. **Core Web Vitals** (Google, 2020/2040) are the standard metrics: **LCP** (Largest Contentful Paint — time to render the largest visible element, should be <2.5s); **INP** (Interaction to Next Paint — latency of user interactions, should be <200ms); **CLS** (Cumulative Layout Shift — visual stability, should be <0.1). **TTFB** (Time to First Byte — server response time). **FCP** (First Contentful Paint — time to render any content). **TBT** (Total Blocking Time — time the main thread is blocked). **Speed Index** (time until visible content is fully rendered). In 2040, **new metrics** include **EPT** (Energy Per Transaction — measuring the carbon cost of page loads) and **ATF** (Above-the-Fold — time to render the viewport-visible content).

**Front-end optimisation** techniques include: **minification** (removing whitespace and comments from CSS and JavaScript); **compression** (Gzip, Brotli, Zstd); **tree shaking** (eliminating unused code); **code splitting** (loading only the code needed for the current page); **lazy loading** (deferring off-screen images and videos); **image optimisation** (WebP, AVIF, responsive images, srcset); **font optimisation** (subset fonts, font-display: swap); **caching** (Cache-Control, Service Workers); and **resource hints** (preconnect, dns-prefetch, prefetch, preload). **Critical CSS** inlines the CSS needed for above-the-fold content, eliminating render-blocking requests. In 2040, **AI-optimised bundlers** (e.g., esbuild with ML-based code splitting) automatically optimise build output based on real user metrics.

**Back-end optimisation** techniques include: **database query optimisation** (indexes, query rewriting, caching); **connection pooling** (reusing database connections); **asynchronous processing** (queues for background jobs); **CDN usage** (caching static assets at edge locations); **edge computing** (running code at CDN edge nodes to reduce latency); **database read replicas** (scaling read traffic); **sharding** (partitioning data across multiple databases); and **caching strategies** (Redis, Memcached, HTTP caching). **Load testing** (Apache JMeter, k6, Locust) simulates traffic to identify bottlenecks before they impact users.

**The 2040 performance landscape** includes **carbon-aware performance optimisation**: reducing data transfer and computation to lower the carbon footprint of web pages. The **Nordic Green Web Initiative** certifies websites that meet energy efficiency standards, and search engines give slight ranking boosts to certified sites. The **Yggdrasil Web Performance Lab** maintains a testbed of real devices (low-end phones, old laptops, slow connections) to ensure that University web properties perform well for all users, not just those with high-end devices.

**Required Reading:**
- Ilya Grigorik, *High Performance Browser Networking*, ch. 10–14
- Steve Souders, *Even Faster Web Sites: Performance Best Practices for Web Developers* (O'Reilly, 2009/2035), ch. 1–4
- Katie Hempenius, "Web Performance Made Easy" (Google I/O, 2035)
- Addy Osmani, "The Cost of JavaScript in 2040" (web.dev, 2040)
- University of Yggdrasil, "Carbon-Aware Web Performance: The Yggdrasil Green Web Certification" (2039)

**Discussion Questions:**
1. Core Web Vitals are standardised by Google and influence search rankings. Does this give Google excessive power over web development practices, or are the metrics genuinely in users' best interests?
2. Carbon-aware performance optimisation reduces data transfer, but it sometimes means serving lower-quality images or reducing functionality. Should websites prioritise carbon efficiency over user experience, or is there a balance?
3. AI-optimised bundlers promise to automatically improve performance, but they are opaque: developers cannot easily understand why the bundler made specific decisions. Is the performance gain worth the loss of developer control?

---

## Lecture 11: Progressive Web Apps, WebAssembly, and the Future of Browser Capabilities

The browser is becoming an increasingly powerful application platform. This lecture covers the technologies that enable app-like experiences in the browser and the emerging capabilities that will shape the web of the 2040s.

**Progressive Web Apps (PWAs)** provide native-app-like experiences using web technologies. **Service Workers** (JavaScript scripts that run in the background) enable offline access, background sync, and push notifications. **Web App Manifest** (a JSON file) defines the app's name, icons, theme, and launch behaviour. **Add to Home Screen** allows PWAs to be installed like native apps. **File System Access API** allows web apps to read and write local files. **Badging API** shows unread counts on app icons. **Contact Picker API** accesses the device's contacts. **Screen Wake Lock API** prevents the screen from sleeping. In 2040, **Project Fugu** (the Chromium initiative to bring native capabilities to the web) has delivered over 50 new APIs, and the gap between web and native apps has narrowed dramatically.

**WebAssembly (Wasm)** is a binary instruction format that runs in the browser at near-native speed. It is not a replacement for JavaScript but a complement: JavaScript orchestrates Wasm modules. **Use cases** include: video editing (FFmpeg in the browser); image manipulation (Photoshop-like editors); scientific simulation (physics engines, molecular dynamics); gaming (Unity, Unreal Engine 5); and cryptography (high-performance encryption/decryption). **Wasm System Interface (WASI)** extends Wasm beyond the browser to server-side and edge environments, enabling portable, sandboxed execution of compiled code. In 2040, **Wasm components** (reusable, interoperable Wasm modules) are the standard for cross-language, cross-platform libraries.

**WebGPU** is the successor to WebGL, providing low-level access to GPU compute capabilities. It enables: real-time ray tracing in the browser; machine learning inference (running TensorFlow.js models on the GPU); scientific visualisation; and high-performance data processing. WebGPU uses the same API concepts as native GPU APIs (Vulkan, Metal, Direct3D 12), making it familiar to graphics programmers. In 2040, **WebGPU is supported** in all major browsers, and it is the standard for browser-based AI inference.

**Emerging web capabilities** in 2040 include: **WebXR** (VR and AR in the browser); **WebTransport** (low-latency bidirectional communication over QUIC); **WebCodecs** (low-level video encoding/decoding); **WebNN** (neural network inference in the browser); **Storage Buckets API** (partitioned, quota-managed storage); **Shared Storage API** (privacy-preserving cross-site data sharing); **Fenced Frames** (embedded content that cannot communicate with its embedder, for privacy-safe advertising); and **Topics API** (interest-based advertising without third-party cookies). These capabilities expand the web's reach but also raise privacy and security concerns that regulators and browser vendors are actively debating.

**Required Reading:**
- Thomas Steiner, "Project Fugu: Bringing Native Capabilities to the Web" (Google I/O, 2035)
- Brian S. Hook, *Programming WebAssembly with Rust* (Pragmatic Bookshelf, 2019/2035), ch. 1–3
- Brandon Jones & Kai Ninomiya, "WebGPU: The Future of Graphics and Compute on the Web" (W3C, 2035)
- Dean Jackson, "WebXR Device API Specification" (W3C, 2035)
- University of Yggdrasil, "The Yggdrasil Virtual Campus: A WebXR Environment for Remote Education" (2039)

**Discussion Questions:**
1. PWAs blur the line between web and native apps. Will PWAs eventually replace native apps, or will native apps always have advantages (better performance, deeper OS integration, stronger security) that keep them relevant?
2. WebAssembly brings near-native performance to the web, but it also enables new attack vectors (Spectre-like side-channel attacks, cryptomining). Is the performance gain worth the security risk?
3. WebXR enables immersive experiences in the browser, but VR headsets are expensive and can cause motion sickness. Is WebXR a genuine educational tool, or is it a gimmick that will be abandoned when the hype fades?

---

## Lecture 12: The Future of the Web — Decentralisation, AI, and the Next Protocol

The final lecture examines the forces that will shape the web in the coming decades: decentralisation, artificial intelligence, and the fundamental protocols that underpin the network.

**Decentralisation** is a reaction to the platform monopolies of the 2010s–2020s. **Blockchain-based systems** (Ethereum, Polkadot, Cosmos) enable decentralised applications (dApps) with transparent, censorship-resistant logic. **IPFS** (InterPlanetary File System) provides decentralised content addressing: files are identified by their hash, not their location, enabling distributed storage and retrieval. **ActivityPub** (W3C standard) powers decentralised social networks (Mastodon, Pleroma, PeerTube). **Matrix** provides decentralised messaging. **Bluesky's AT Protocol** separates identity, data, and algorithm, enabling users to choose their content curation algorithms. In 2040, **the federated web** is a viable alternative to centralised platforms, though network effects and convenience keep centralised platforms dominant for mainstream users.

**AI and the web** are increasingly intertwined. **AI-generated content** (text, images, video, audio) fills the web, raising questions of authenticity, copyright, and trust. **AI-personalised interfaces** adapt websites to individual users in real time, optimising for engagement, comprehension, or conversion. **AI-assisted search** (ChatGPT, Perplexity, and the University's *Mímir Search*) provides conversational answers rather than link lists, transforming how users discover information. **AI-driven development** (GitHub Copilot, Devin, and the University's *Skald*) generates web applications from natural language descriptions, accelerating development but also raising concerns about code quality and security. In 2040, **the AI-native web** — where AI agents browse, interact, and transact on behalf of users — is an emerging paradigm that may reshape the web as profoundly as the mobile revolution did.

**The next protocol** after HTTP/3 is already being researched. **HTTP/4** (not yet standardised as of 2040) may introduce: **binary request bodies** for more efficient serialisation; **multicast HTTP** for efficient content delivery to millions of simultaneous viewers; **negotiable compression** (allowing clients and servers to agree on compression algorithms); and **integrated AI negotiation** (servers advertising AI capabilities, clients requesting AI-enhanced content). More radically, some researchers propose replacing HTTP entirely with **Named Data Networking (NDN)** — a content-centric protocol where requests are for named data rather than specific servers, naturally supporting caching, multicast, and mobility. The University of Yggdrasil's **Future Internet Lab** operates an experimental NDN testbed alongside the traditional HTTP infrastructure.

**Required Reading:**
- Juan Benet, "IPFS — Content Addressed, Versioned, P2P File System" (2014/2035)
- Tim Berners-Lee, "The Next Web" (TED Talk, 2009/2035) and "The Semantic Web Revisited" (2035)
- Mike Masnick, "Protocols, Not Platforms: A Technological Approach to Free Speech" (Knight First Amendment Institute, 2019/2035)
- Lixia Zhang et al., "Named Data Networking," *ACM SIGCOMM Computer Communication Review* 44, no. 3 (2014): 66–73
- University of Yggdrasil, "The Future Internet Lab: HTTP/4, NDN, and the Next Generation of Web Protocols" (2039)

**Discussion Questions:**
1. Decentralised platforms promise freedom from corporate control, but they also struggle with moderation, spam, and user experience. Is decentralisation a realistic future for the web, or will centralised platforms always dominate due to their superior resources and convenience?
2. AI-generated content is flooding the web, making it harder to distinguish truth from fabrication. Should the web adopt a "provenance" system that tracks the origin and editing history of all content, or would this be an unacceptable surveillance mechanism?
3. Named Data Networking replaces server-centric communication with content-centric communication. Is NDN a genuine improvement over HTTP, or does it merely shift complexity from the application layer to the network layer?

---

## Final Examination Preparation

The final examination for IT107 is a **practical project** (60% of grade) combined with a **written theory exam** (40% of grade).

**Practical Project (60%):**
Students build and deploy a complete web application for a real or fictional organisation. The application must: use semantic HTML, modern CSS (Flexbox/Grid), and TypeScript; include a backend API (Node.js or Python) with database persistence; implement authentication and authorisation; be responsive and accessible (passing WCAG 2.1 AA); be deployed to the Yggdrasil Cloud using containers and CI/CD; and include documentation (README, API docs, architecture diagram). The project is evaluated on functionality, code quality, security, performance, accessibility, and deployment professionalism.

**Written Theory Exam (40%):**
Choose 4 of 8 essay questions:

1. Trace the evolution of the web from a document system to an application platform. For each era, identify the technical innovations and the business models that drove adoption. Is the web's evolution complete, or is another paradigm shift imminent?

2. HTTP/3 uses QUIC instead of TCP. Explain the differences between TCP and QUIC, and analyse the benefits and challenges of this transition. Will QUIC eventually replace TCP for all applications, or will the two coexist?

3. CSS Grid and Flexbox have transformed web layout, but many developers still struggle with them. Are these layout systems genuinely intuitive, or do they require a mental model shift that some developers find difficult?

4. Compare REST, GraphQL, and gRPC as API design paradigms. For what types of applications is each best suited? Is one paradigm likely to dominate the others, or will they coexist indefinitely?

5. Web security vulnerabilities (SQL injection, XSS, CSRF) have been known for decades, yet they remain common. Are developers not learning from past mistakes, or are new developers constantly entering the field and repeating old errors?

6. PWAs, WebAssembly, and WebGPU are bringing native-like capabilities to the browser. Will the browser eventually become the universal application runtime, or will native platforms always have advantages?

7. AI is transforming the web through generated content, personalised interfaces, and assisted development. Is the AI-native web an enhancement of human capability or a replacement of human agency?

8. Decentralised protocols (IPFS, ActivityPub, NDN) challenge the centralised web. Analyse their technical merits and practical limitations. Will the future web be more decentralised or more centralised than today?

**Grading:**
- A (Excellent): A fully functional, secure, accessible, and well-documented web application with clean architecture and professional deployment. Written exam demonstrates deep understanding of web technologies and their societal implications.
- B (Good): A functional web application with minor gaps in security, accessibility, or documentation. Written exam is competent but lacks critical depth.
- C (Satisfactory): A web application that meets minimum requirements but has significant gaps. Written exam shows basic understanding but limited analysis.
- D (Poor): A partially functional web application or one with serious security or accessibility flaws. Written exam is superficial or contains errors.
- F (Fail): No functional web application or missing project. Written exam fails to demonstrate understanding of web technologies.

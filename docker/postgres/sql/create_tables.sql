CREATE TABLE Category (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    description TEXT
);

INSERT INTO Category (title, description) VALUES
('Hardware', 'Reviews, news, and guides on the latest computer hardware, components, and peripherals.'),
('Operating Systems', 'Tutorials and updates on various operating systems, including Windows, Linux, and macOS.'),
('Mobile Development', 'Resources and tutorials for developing mobile applications on iOS and Android platforms.'),
('Web Development', 'Tips, tutorials, and best practices for building websites and web applications.'),
('AI Ethics', 'Discussions on the ethical implications and considerations of artificial intelligence.'),
('IT Careers', 'Advice, interviews, and guides for building a successful career in IT.'),
('Gadgets', 'News and reviews of the latest gadgets and consumer electronics.'),
('Virtual Reality', 'Insights and news about VR technologies and applications.'),
('Blockchain', 'Articles and tutorials on blockchain technology, cryptocurrencies, and decentralized applications.'),
('Quantum Computing', 'Information and discussions on the advancements and applications of quantum computing.');



CREATE TABLE Tag (
    id SERIAL PRIMARY KEY,
    name VARCHAR(100) NOT NULL,
    description TEXT
);

INSERT INTO Tag (name, description) VALUES
('Cloud Computing', 'Articles and tutorials about cloud platforms, services, and technologies including AWS, Azure, Google Cloud, and more.'),
('Cybersecurity', 'Insights, news, and best practices related to securing information systems and protecting data from cyber threats.'),
('Data Science', 'Posts about data analysis, machine learning, artificial intelligence, and data visualization techniques and tools.'),
('DevOps', 'Content focusing on practices and tools that combine software development and IT operations to improve efficiency and deployment.'),
('Programming', 'Tutorials, tips, and best practices for various programming languages such as Python, JavaScript, Java, C#, and more.'),
('Networking', 'Information and guides on network infrastructure, protocols, configurations, and troubleshooting.'),
('Software Development', 'Topics covering the software development lifecycle, methodologies, tools, and project management techniques.'),
('Tech News', 'Updates and commentary on the latest trends, products, and innovations in the technology industry.'),
('Database Management', 'Articles about database design, SQL, NoSQL, and best practices for managing and optimizing database systems.'),
('Artificial Intelligence', 'Discussions and tutorials on AI concepts, applications, advancements, and ethical considerations.');


CREATE TABLE Users (
    id SERIAL PRIMARY KEY,
    first_name VARCHAR(100) NOT NULL,
    last_name VARCHAR(100) NOT NULL,
    email VARCHAR(100) NOT NULL,
    password VARCHAR(100) NOT NULL,
    middle_name VARCHAR(100),
    created_at TIMESTAMP DEFAULT NOW(), 
    updated_at TIMESTAMP,
    UNIQUE (email)
);

--- ADD FAKE USER, TODO: Remove when the app is fully functional ---
INSERT INTO Users (first_name, last_name, email, password, middle_name) VALUES
('fake_name', 'fake_lastname', 'fake_email', 'fake_password', 'fake_middle_name');

CREATE TABLE Post (
    id SERIAL PRIMARY KEY,
    title VARCHAR(100) NOT NULL,
    content TEXT NOT NULL,
    created_by VARCHAR(100) NOT NULL,
    published_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP,
    FOREIGN KEY (created_by) REFERENCES Users(email)
);

CREATE TABLE PostTags (
    id SERIAL PRIMARY KEY,
    post_id INTEGER NOT NULL,
    tag_id INTEGER NOT NULL,
    FOREIGN KEY (post_id) REFERENCES Post(id) ON DELETE CASCADE,
    FOREIGN KEY (tag_id) REFERENCES Tag(id) ON DELETE CASCADE,
    UNIQUE (post_id, tag_id)
);

CREATE TABLE PostCategories (
    id SERIAL PRIMARY KEY,
    post_id INTEGER NOT NULL,
    category_id INTEGER NOT NULL,
    FOREIGN KEY (post_id) REFERENCES Post(id) ON DELETE CASCADE,
    FOREIGN KEY (category_id) REFERENCES Category(id) ON DELETE CASCADE,
    UNIQUE (post_id, category_id)
);
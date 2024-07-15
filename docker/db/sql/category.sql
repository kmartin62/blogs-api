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

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
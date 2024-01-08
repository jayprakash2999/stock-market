# Use this to populate the database

[
  {
    "Name": "ABC Corporation",
    "Symbol": "ABC",
    "Sector": "Technology",
    "Industry": "Software",
    "Description": "A leading software development company.",
    "MarketCap": 5000000000,
  },
  {
    "Name": "XYZ Healthcare",
    "Symbol": "XYZ",
    "Sector": "Healthcare",
    "Industry": "Biotechnology",
    "Description": "Specializing in innovative biotech solutions.",
    "MarketCap": 3000000000,
  },
  {
    "Name": "123 Financial Services",
    "Symbol": "123",
    "Sector": "Financial",
    "Industry": "Banking",
    "Description": "Providing a wide range of financial services.",
    "MarketCap": 8000000000,
  },
  {
    "Name": "Tech Innovators Inc.",
    "Symbol": "TI",
    "Sector": "Technology",
    "Industry": "Electronics",
    "Description": "Pioneering new technologies in the electronics sector.",
    "MarketCap": 7000000000,
  },
  {
    "Name": "Green Energy Solutions",
    "Symbol": "GES",
    "Sector": "Energy",
    "Industry": "Renewable Energy",
    "Description": "Leading the way in sustainable and green energy solutions.",
    "MarketCap": 6000000000,
  },
{
    "Name": "XBC Corporation",
    "Symbol": "XBC",
    "Sector": "Manufacturing",
    "Industry": "Electronics",
    "Description": "A leading manufacturing company in the electronics sector.",
    "MarketCap": 6000000000,
  }
]

#     CREATE TABLE IF NOT EXISTS company_details (
#     id INT AUTO_INCREMENT PRIMARY KEY,
#     name VARCHAR(255) NOT NULL,
#     symbol VARCHAR(10) NOT NULL UNIQUE,
#     sector VARCHAR(50) NOT NULL,
#     industry VARCHAR(50) NOT NULL,
#     description TEXT NOT NULL,
#     market_cap BIGINT NOT NULL
# );


# INSERT INTO company_details (name, symbol, sector, industry, description, market_cap)
# VALUES
#   ('ABC Corporation', 'ABC', 'Technology', 'Software', 'A leading software development company.', 5000000000),
#   ('XYZ Healthcare', 'XYZ', 'Healthcare', 'Biotechnology', 'Specializing in innovative biotech solutions.', 3000000000),
#   ('123 Financial Services', '123', 'Financial', 'Banking', 'Providing a wide range of financial services.', 8000000000),
#   ('Tech Innovators Inc.', 'TI', 'Technology', 'Electronics', 'Pioneering new technologies in the electronics sector.', 7000000000),
#   ('Green Energy Solutions', 'GES', 'Energy', 'Renewable Energy', 'Leading the way in sustainable and green energy solutions.', 6000000000),
#   ('XBC Corporation', 'XBC', 'Manufacturing', 'Electronics', 'A leading manufacturing company in the electronics sector.', 6000000000);

# Mini Ingestion Pipeline and Reporting

This repo is a in-progress ingestion pipeline for a small tech shop. They are mostly using SaaS products, so they receive data daily from different source systems.

They use passbook for their customer database, so they receive a **full file daily** of their customers in csv format. Their products are stored on a small web page, and a product catalog is pulled daily as a **full file** in json format.
Their sales come from a legacy ACH server, so it sends **transactional data** in a tilde delimited format.

The dev team has mostly finished this pipeline, but the dev was having a few problems and needs your help to finish it. The current statuses:

| Pipeline  | Status      |
| --------- | ----------- |
| Customers | Done        |
| Sales     | In progress |
| Product   | To Do       |

As well as this, there are a few open tickets:

- [Ticket MIDP-307](./Ticket%201.md)
- [Ticket MIDP-313](./Ticket%202.md)

## Context

The pipeline is fairly straight-forward. Files arrive into the `landing_zone` folder, (and you should have 1 week's worth of files). The first step splits and organizes the files into their proper folders for archiving, and the second step
processes the data. Since we don't want to deal with databases, we are using Apache Parquet format as a small mini table.

The data is stored with a Slowly Changing Dimension (Type 2), by adding a few columns to each row to keep track of changes over time. This way we can see the state of the system at every point in time.

After that we can use these generated parquet files to make some simple charts or some csv files.

## Test Instructions

1. ### Clone and save the repo

   a. Clone this repo to your local environment.

   b. Make a copy of this repo in your account before making any changes.

   > This is important as it is easy to delete data and you may need to revert back to the initial commit.

   c. Follow the setup instructions.

2. ### Tasks

   > **Important** - Remember to commit your code changes after each complete task.

   a. **Run the `workbook.ipynb` notebook**. It should error out on the second report. The first report should match the image [customer_growth.png](./final_results/customer_growth.png)

   b. **Fix the sales pipeline**. **This will require no new lines of code**. The fixes will simply be mistakes throughout the pipeline that needs editing. Start with uncommenting `line 30` in `src/configs/file_configs.py` and running the
   workbook.

   > You will know you got it to work properly when the second report works and matches [sales_by_membership.png](./final_results/sales_by_membership.png)

   c. **Implement the product pipeline.** This involves adding the json files into the ingestion in a way that matches the same code patterns used for the other two pipelines. Start by creating a config in `./src/configs/file_configs.py`
   that uses the `./src/configs/schemas.py:PRODUCT_SCHEMA`.

   > You will know it works when the third report, a dataframe, matches the exported csv [product_sale_breakdown.csv](./final_results/product_sale_breakdown.csv)

   d. **Complete the two tickets**. There are two markdown files:

   - [Ticket 1.md](./Ticket%201.md)
   - [Ticket 2.md](./Ticket%202.md)

   Complete both of them in whatever way you feel is best. For the second ticket, there is already some placeholder code in `./src/utils/validation.py` as well as schemas to use in `./src/configs/schemas.py`.

   e. (Optional)

   Show off! Do something interesting or fun and document what you've done. This is optional if you are pressed for time, but this is a great opportunity to show off some interesting python or other skills based off this project.

3. ### Push your code to your account

   This can be a new account, but you will get bonus points if you push it to your portfolio account with your other work. Submit the github repo url to the email provided in the instruction set that led you to this repo.

---

## Setup

- Clone this repo to your local environment
- Create a virtual environment

  ```bash
  python -m venv .venv
  ```

- Activate the environment  
   On mac or linux:

  ```bash
  source ./.venv/bin/activate
  ```

  On Windows

  ```bash
  ./.venv/Scripts/Activate.bat
  ```

- Install requirements

  ```bash
  pip install -r requirements.txt
  ```

## Helpful Tips

If you're using VS Code, make sure the `Jupyter` extension is installed.

Since python caches imports, remember to restart the kernel in the notebook if you make changes in the imported files.

You can use `reload.ipynb` to quickly move all the files back into the `landing_zone` folder to make it easier to rerun the files.

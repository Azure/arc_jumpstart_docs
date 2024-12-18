# Predictive Analytics - Appendix

## Prompt examples

> **Note**: The following table provides example prompts and expected results.  Note that the output will likely vary somewhat from this table, but the overall analysis should be similar.

| Prompt Text | Expected Result | Source Data | Remarks |
|-------------|-----------------|-------------|---------|
| _"Based on the sales data in this spreadsheet, how many bananas have I sold?"_ | we've sold 1,339 bananas | `retail_inventory_sample` | Note that we did not specify the specific product name; just bananas |
| _"Based on the sales data for apples, which locations in the store sell the most apples?"_ | Stock Locations 1, 2, and 3 are the top locations for selling apples, each selling 25 apples per day, while Stock Location 4 sells 15 apples per day | `retail_inventory_sample` |
| _"Provide a summary of coffee roasting production."_ | Overview of coffee roasting production metrics. | `contoso_roasters` | Check for any missing logs |
| _"How many chocolate chip cookies did I sell each day?"_ | a list of cookies sold per day | `retail_inventory_sample` |
| _"How many chocolate chip cookies went unsold each day?"_ | a count of the cookies left unsold each day | `retail_inventory_sample` |
| _"Based on the chocolate chip cookie sales data, which day of the week generates the most cookie sales?"_ | Copilot identifies that most cookies sales are on Friday | `retail_inventory_sample` |
| _"Which day of the week generates the most unsold chocolate chip cookies?"_ | Copilot identifies that Thursdays have the most unsold cookies | `retail_inventory_sample` |
| _"Which location in the store produces the least amount of sales?"_ | Copilot identifies that Stock Location 4 generates the least amount of sales  | `retail_inventory_sample` |
| _"Which store location sells the most cookies?"_ | Copilot identifies that Stock Location 2 sells the most cookies | `retail_inventory_sample` |
| _"This spreadsheet contains footfall data for each store location. Footfall is the number of people at each store location. Based on this data, which store location has the most footfall?"_ | Copilot indicates that Stock Location 2 has the most footfall | `footfall_sample` |
| _"What correlations do you observe between footfall and sales?"_ | Copilot observes a correlation between higher footfall traffic with higher sales and that locations with consistent footfall have consistent sales | `retail_inventory_sample` and `footfall_sample` | Note that it is making correlation between these two spreadsheets without explicitly joining tables |
| _"If I can increase footfall to 800, how many chocolate chip cookies should I expect to sell?"_ | Copilot assumes a linear relationship between footfall and sales and estimates we could sell 100 cookies per day with increased footfall | `retail_inventory_sample` and `footfall_sample` | While not intended to replace the role of a data scientist, Copilot is able to suggest an estimate based on the relationship between the data in both spreadsheets |
| _"Using the `roast_start_time` and `cooling_end_time` columns, what's the total amount of hours and minutes my Probat roaster has been used so far?"_ | Copilot lists the roast duration for each day and adds of the total roast time | `contoso_roasters` | This is helpful for tracking periodic maintenance tasks that need to occur |
| _"Which roast profile should I use for City Plus roasts that produces the least amount of moisture loss?"_ | Copilot identifies roast profile_cp_01 as the roast that produces the least amount of moisture loss| `contoso_roasters` | Everything else equal, it's desirable to use the roast profile that produces the least amount of moisture loss because it means there's more salable product for an equally good product |
| _"How much energy have I used for all of my roasts this month?"_ | Copilot adds the data in the for power consumption| `contoso_roasters` | Note that Copilot is able to identify the pertinent field from the spreadsheet to answer this question |
| _"How many kilograms of Tanzanian beans have I roasted?"_ | Copilot lists the two days where this bean type was roasted and lists the total amount roasted | `contoso_roasters` |
| _"How many kilograms of beans from Mexico have I roasted this month?"_ | Copilot identifies the two varieties of Mexican beans roaster and lists the total amount roasted | `contoso_roasters` | Note that Copilot does not need to be explicitly told about the Mexican bean varieties |
| _"Which coffee stays on the store shelves the longest?"_ | Copilot identifies that the Tanzanian beans is unsold and stays on the shelves the longest | `contoso_roasters` |
| _"If current sales trends of coffee continues, how much Mexican beans should I order for roasting?"_ | Copilot estimates average daily sales, projects it over a month, and suggests a quantity of Mexican beans to order | `contoso_roasters` and `retail_inventory_sample` |
| _"How much beans from Tanzania should I order if I except a 10% increase in demand for these beans over the next month?"_ | Copilot looks at the two different roasts of Tanzanian beans and estimates the demand for each based on a 10% increase in demand | `contoso_roasters` and `retail_inventory_sample` |
